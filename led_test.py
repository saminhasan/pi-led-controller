from rpi_ws281x import *
import numpy as np
import time
import sys
# LED strip configuration:
LED_COUNT      = 48      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 127     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()
try:
        while True:
                datas = np.random.randint(0,255, size=(LED_COUNT,3), dtype=np.uint32)
                for idx,data in enumerate(datas):
                        strip.setPixelColor(idx,Color(int(data[0]),int(data[1]),int(data[2])))
                strip.show()
                time.sleep(0.1)
except KeyboardInterrupt:
        for idx in range(LED_COUNT):
                strip.setPixelColor(idx,Color(0,0,0))
        strip.show()
        print("\nExit")
        sys.exit(0)