import RPi.GPIO as g
import os
import time
g.setmode(g.BOARD)

g.setup(11,g.IN,pull_up_down=g.PUD_DOWN)

g.setup(37,g.OUT)

g.output(37,False)

try:
	while True:
		time.sleep(0.02)
		if g.input(11)==1:
			check=True
		else :
			check=False

		g.output(37,check)
	
except KeyboardInterrupt:
	g.cleanup()

