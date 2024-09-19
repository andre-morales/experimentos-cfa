import network
import machine
from machine import Pin, I2C
import time
import ssd1306 
import network
import helloServer

HOSTNAME='muitobom'
WIFI_NAME='lab8'
WIFI_PASSWORD='...'

def main():
	connectToWAP()
	beginServer()

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

def beginServer():
	# Try hosting the web server from port 5000 onwards.
	port = 5000
	tries = 50
	while tries > 0:
		try:
			helloServer.run(port)
			break
		except OSError as err:
			# Only catch port binding errors, let any other exception propagate.
			if err.errno == 112:
				print("Failed to bind to port.")
				port += 1
				tries -= 1
			else:
				raise err

def connectToWAP():
	#  Enable Wi-Fi as a client 
	print("Enabling Wi-Fi...")
	wifi = network.WLAN(network.STA_IF)
	wifi.active(True)

	# Configure the .local hostname and try connecting to the network
	print("Trying to connect to", WIFI_NAME, "...")
	wifi.config(dhcp_hostname=HOSTNAME)
	wifi.connect(WIFI_NAME, WIFI_PASSWORD)

	# Wait for a connection success (or failure)
	while not wifi.isconnected():
		pass
	
	# Print the connection status
	host = wifi.config('dhcp_hostname')
	print('Connected as {}/{}, net={}, gw={}, dns={}'.format(
		host, *wifi.ifconfig()))

main()