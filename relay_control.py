import pigpio

pi = None



def turn_on_pin(pin):
  pi.write(pin, constants.HIGH)
  return True

def turn_off_pin(pin):
  pi.write(pin, constants.LOW)