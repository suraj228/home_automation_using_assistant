import logging
import json

pi = None
pigpio = None
ERR_CODES = None

def initPi():
	try:
		global pi, pigpio
		pigpio = __import__("pigpio")
		pi = pigpio.pi()
	except Exception as e:
		logging.error("initPi errror: %s", e)

initPi()
print(pi)