import logging
import json

pi = None
RPi.GPIO = None
ERR_CODES = None

def initPi():
    try:
        global pi, RPigpio
        RPi.GPIO = __import__("RPi.GPIO")