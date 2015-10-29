#!/usr/bin/python
import RPi.GPIO as g
import time
led=36
g.setmode(g.BOARD) 
g.setup(led,g.OUT)
g.output(led, 1)
#g.cleanup()