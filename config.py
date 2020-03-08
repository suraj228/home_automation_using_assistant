import os
import json 
import logging

CONFIG = {}

def readConfig(file):
  global CONFIG
  try:
    configFile = open(file, "r")
    configure = configFile.read()
    cfg = json.loads(configure)

    CONFIG = cfg

  except Exception as e:
    logging.error("readConfig error : %s", e)

def getConfig(obj = None, attr = None):
    global CONFIG
    try:
        if(obj == None):
            return CONFIG
        elif(attr != None):
            return CONFIG[obj][attr]
        else:
            return CONFIG[obj]
    except:
        logging.error("Failed to get config")
