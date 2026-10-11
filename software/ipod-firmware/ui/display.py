from machine import Pin, SoftSPI
import st7789py as st7789

def init_display():
    cs_pin = Pin(27, Pin.OUT)
    dc_pin = Pin(21, Pin.OUT)
    rst_pin = Pin(19, Pin.OUT)
    scl_pin = Pin(32, Pin.OUT)
    sda_pin = Pin(33, Pin.OUT)

    spi = SoftSPI(
        baudrate = 40000000,
        polarity = 1,
        phase = 1,
        sck = scl_pin,
        mosi = sda_pin,
        miso = scl_pin
    )

    display = st7789.ST7789(
        spi,
        320,
        240,
        reset = rst_pin,
        dc = dc_pin,
        cs = cs_pin,
        rotation = 1
    )

    return display