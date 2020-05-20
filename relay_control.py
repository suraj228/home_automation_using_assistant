import utils
import constants
from importlib import import_module
configMod = import_module("config")


pi = None
all_pins = []
for _ in range(2,17):
  global all_pins
  all_pins.append(_)

def getPi():
  global pi
  pi = utils.initPi()

def turn_on_pin(pin):
  if(pin == 0):
    for i in all_pins:
      pi.write(i, constants.HIGH)
  pi.write(pin, constants.HIGH)
  return True

def turn_off_pin(pin):
  if(pin == 0):
    for i in all_pins:
      pi.write(i, constants.LOW)
  pi.write(pin, constants.LOW)
  return True
  
getPi()
