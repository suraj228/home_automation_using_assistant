# used for logging 
import logging
# importing all required modules
from importlib import import_module
from Adafruit_IO import Client, Feed, Data 
import constants
import config as cfg

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
  while True:
    d = aio.receive('ldr')
    logging.info('data recieved')
    # the recieved d(data) will be in object form we just need the value
    data = (d.value)
    # To reduce simply iterating and controlling pins
    if(previous_data == None):
      previous_data = data
    else:
      logging.info('value recieved: %s', data)
      if(previous_data == data):
        continue
    print(data)
    if(data == 0):
      
      print(0)
      continue
    elif(data == 1):
      print("1")
      continue
    elif(data == 17):
      print("17")
      continue

main()