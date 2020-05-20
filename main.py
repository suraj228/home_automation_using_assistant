# used for logging 
import logging
# importing all required modules
from importlib import import_module
from Adafruit_IO import Client, Feed, Data 
import constants
import utils
import json
import relay_control as re
from importlib import import_module
configMod = import_module("config")


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('google_assistant_automation.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logging.info("Program started")


def main():
  logging.info("main started")
  aio = Client(constants.USERNAME, constants.AIO_KEY)
  # if feed not used since long time it results in error while reading so send dummy data to keep feed active
  # here ldr is the name of the feed created in adafruit io
  aio.send('ldr', 0)
  previous_data = None
  t_light = configMod.getConfig("tube_light")
  print(t_light)
  while True:
    d = aio.receive('ldr')
    logging.info('data recieved')
    # the recieved d(data) will be in object form we just need the value
    data = int(d.value)
    # To reduce simply iterating and controlling pins
    if(previous_data == None):
      previous_data = data
    else:
      logging.info('value recieved: %s', data)
      if(previous_data == data):
        continue
    print(data)
    
    if(data == 0):
      
      re.turn_off_pin(data)
      continue
    elif(data == 1):
      print("1")
      continue
    elif(data == 2):
      print("2")
      continue
    elif(data == 3):
      pass
      continue
    elif(data == 4):
      pass
    continue



main()