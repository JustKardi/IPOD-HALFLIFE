import time
import gc
from ui.display import init_display
from audio import init_audio, play_wav, stop_audio

gc.enable()

lcd = init_display()

audio = init_audio(rate=44100, bits=16, channels=2)

try:
    print("Playing system sound track...")
    play_wav(audio, "boot.wav")
    
except Exception as e:
    print("Audio file playback error:", e)

while True:
    time.sleep(1)
