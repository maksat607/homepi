#!/usr/bin/python
import sys
import RPi.GPIO as g
import time
g.setmode(g.BOARD)
pin=int(sys.argv[3])
g.setup(pin,g.OUT)
g.output(pin,int(sys.argv[1]))
time.sleep(int(sys.argv[2])*60)
g.cleanup()

