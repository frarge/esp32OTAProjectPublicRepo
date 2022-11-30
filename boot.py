# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
import network
import senko
import machine

GITHUB_URL = "https://github.com/frarge/esp32project/"
OTA = senko.Senko(url=GITHUB_URL, files=["boot.py", "main.py"])

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('TIM-19910111', 'Semipaghitelado.95')
    while not wlan.isconnected():
        pass
    print('network config:', wlan.ifconfig())

if OTA.update():
    print("Updated to the latest version! Rebooting...")
    machine.reset()

webrepl.start(password = "frarge95")