from machine import I2S, Pin

PCM_DIN = 22
PCM_BCK = 26
PCM_LRCK = 25

def init_audio(rate=44100, bits=16, channels=2):
    audio_out = I2S(
        0,
        sck=Pin(PCM_BCK),
        ws=Pin(PCM_LRCK),
        sd=Pin(PCM_DIN),
        mode=I2S.TX,
        bits=bits,
        format=I2S.STEREO if channels == 2 else I2S.MONO,
        rate=rate,
        ibuf=10240
    )
    return audio_out

def play_wav(audio_device, file_path):
    buffer = bytearray(2048)

    with open(file_path, "rb") as wav_file:
        if (file_path.endswith(".wav")):
            wav_file.seek(44)

        while True:
            bytes_read = wav_file.readinto(buffer)

            if bytes_read == 0:
                break

            audio_device.write(buffer[:bytes_read])

def stop_audio(audio_device):
    audio_device.deinit()