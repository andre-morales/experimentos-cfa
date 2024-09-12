import network
import machine

from machine import Pin, I2C
import time
import ssd1306 # https://github.com/micropython/micropython-esp32/blob/esp32/drivers/display/ssd1306.py
import network

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.config(dhcp_hostname='muitobom')
wifi.connect('lab8', 'lab8arduino')
wifi.config(dhcp_hostname='muitobom')

while not wifi.isconnected():
    pass

host = wifi.config('dhcp_hostname')
print('Wifi connected as {}/{}, net={}, gw={}, dns={}'.format(
    host, *wifi.ifconfig()))

import helloServer

'''
i2c=I2C(sda=Pin(5), scl=Pin(4))
display=ssd1306.SSD1306_I2C(128,64,i2c)
x = 0
while True:
    display.fill(0)
    display.text('hello, world!', x - 128, 20, 1)
    display.show()
    x = (x + 1) % 256
'''
    
#  display.fill(1)
#  display.show()
#  time.sleep(1)
#  display.fill(0)
#  display.text("Am I blinking?",10,10,1)
#  display.show()
#  time.sleep(1)
#  display.fill(0)

# sta = network.WLAN(network.AP_IF)
# sta.active(True)
# sta.config(essid="aiaiai", password='senha')*/
