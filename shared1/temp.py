#!/usr/bin/python
import RPi.GPIO as g
import Adafruit_DHT
import time
import MySQLdb

sensor = Adafruit_DHT.DHT22
led=11
g.setmode(g.BOARD) 
g.setup(led,g.OUT)
g.setup(37, g.OUT) 
g.output(37, False)
dt = list(time.localtime())
turn=True
check=True
pin = 4
f = open("/media/"+`dt[0]`+'-'+`dt[1]`+'-'+`dt[2]`+'.txt','w')
db = MySQLdb.connect(host='localhost',user='root',passwd='maksat',db='my_db') # name of the data base
cur = db.cursor() 
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

try:
	while True:
		dt = list(time.localtime())
		humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
		if humidity is not None and temperature is not None:
			time.sleep(2)
			f.write( "["+`dt[3]`+":"+`dt[4]`+"]  ")
			f.write('Temp={0:0.1f}*C  Humidity={1:0.1f}%\n'.format(temperature, humidity)) 
			str='insert into temperature values  (NULL,{0:0.1f},{1:0.1f},(select now()))'.format(temperature, humidity)
			query=(str)
			cur.execute(query)
			db.commit()
			print  "["+`dt[3]`+":"+`dt[4]`+']  Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
			if temperature<25 and turn:
				turn=False
				g.output(37, True)
			elif temperature>27 and turn==False:
				turn=True
				g.output(37, False)			
		else:
			print 'Failed to get reading. Try again!'
			
except KeyboardInterrupt:
	g.cleanup()
	f.close()
	db.close()

