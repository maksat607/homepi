#!/usr/bin/python
import sys
import RPi.GPIO as g
import time
g.setmode(g.BOARD)
pin=13
g.setup(pin,g.OUT)
g.output(pin,int(sys.argv[1]))
#time.sleep(3000)
#g.cleanup()

