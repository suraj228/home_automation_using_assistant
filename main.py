import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('googleassistantiot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logging.info("main logging statrted")
from importlib import import_module
from Adafruit_IO import Client, Feed, Data 
import constants
import os
cwd = os.getcwd()
configMod = import_module("config")
def main():
  logging.info("main started")
  aio = Client(constants.USERNAME, constants.AIO_KEY)
  aio.send('ldr', 0)
  while True:
    d = aio.receive('ldr')
    data = (d.value)
    print(data)
    if(data == 0):
      print(0)
    elif(data == 1):
      print("1")
    elif(data == 17):
      print("17")

main()