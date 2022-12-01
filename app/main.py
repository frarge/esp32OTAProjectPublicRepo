from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)
while True:
  print("Hello World")
  sleep(3000)