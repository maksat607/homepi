#!/usr/bin/python
import RPi.GPIO as g
import time
import sys
g.setmode(g.BOARD)
pin=11
g.setup(pin,g.OUT)
g.output(pin,int(sys.argv[1]))
#time.sleep(2)
#g.cleanup()

