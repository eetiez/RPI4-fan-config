#!/usr/bin/python

import smbus
import os
import time
from threading import Thread

bus = smbus.SMBus(1)

def get_fanspeed(tempval, configlist):
	for curconfig in configlist:
		curpair = curconfig.split("=")
		tempcfg = float(curpair[0])
		fancfg = int(float(curpair[1]))
		if tempval >= tempcfg:
			return fancfg
	return 0

def temp_check():
	fanconfig = ["65=100", "60=55", "55=10"]
	address=0x1a
	prevblock=0
	while True:
		temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
		val = float(temp)/1000
		block = get_fanspeed(val, fanconfig)
		if block < prevblock:
			time.sleep(30)
		prevblock = block
		try:
			bus.write_byte(address,block)
		except IOError:
			temp=""
		time.sleep(30)

try:
	t = Thread(target = temp_check)
	t.start()
except:
	t.stop()