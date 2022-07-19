from multiprocessing.connection import Listener
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
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

PORT = 1234
IP = '0.0.0.0'

def set_led(datas):
        #print(type(datas), datas.shape)
        for idx,data in enumerate(datas):
                strip.setPixelColor(idx,Color(int(data[0]),int(data[1]),int(data[2])))
        strip.show()

class LEDserver:
        def __init__(self, ip, port):
                self.running = True
                self.listener = Listener((ip, port))
                self.connection = None
                self.connect()

        def connect(self):
                data = np.zeros((LED_COUNT,3),dtype=int)
                data[:,0] = 255
                set_led(data)
                print("Waiting for connection")
                try:
                        self.connection = self.listener.accept()
                        self.run()

                except KeyboardInterrupt:
                        print("\nUser Exit")
                        self.close()

                except Exception as e:
                        print(e)

        def run(self):
                print("Server Started")
                try:
                        while self.running:
                                data = self.connection.recv()
                                set_led(data)

                except EOFError:
                        print("No data -> setting LEDS to off and restarting server")
                        self.connection.close()
                        self.connect()

                except KeyboardInterrupt:
                        print("\nUser Exit")
                        self.close()

        def close(self):
                if self.connection:
                        self.connection.close()
                self.listener.close()
                data = np.zeros((LED_COUNT,3),dtype=int)
                set_led(data)
                sys.exit(0)

if __name__ == '__main__':
        server = LEDserver(IP, PORT)