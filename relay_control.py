import pigpio

pi = None

def initPi():
  pi = pigpio.pi()
  return pi