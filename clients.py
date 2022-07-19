from led_client import LEDclient
import colorsys
import numpy as np
import time
LED_COUNT=48
PORT = 1234

addresses = ['192.168.10.101', '192.168.10.102', '192.168.10.103']

clients = []
for address in addresses:
	client = LEDclient(address,PORT)
	clients.append(client)
	

counter = 0 
try:
	while True:
		for idx, client in enumerate(clients):
			datas=np.zeros((LED_COUNT,3))
			n, m = datas.shape
			
			for lid in range(n):
				x = (lid + counter) % n
				r, g, b = colorsys.hls_to_rgb(1, 0.1, (x/LED_COUNT))
				datas[lid, 0] = np.clip(r * 255, 0, 255)
				datas[lid, 1] = np.clip(g * 255, 0, 255)
				datas[lid, 2] = np.clip(b * 255, 0, 255)
		
			client.send_data(datas)
			
		counter += 1
		#counter += 1

		time.sleep(0.01)

except KeyboardInterrupt:
		print("\nUser Interrupt")
		
except Exception as e:
	print("ERROR : ", e)

	