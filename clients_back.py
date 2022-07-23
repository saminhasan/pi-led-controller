from led_client import LEDclient
import numpy as np
import time
LED_COUNT=48
PORT = 1234

# addresses = ['192.168.10.101', '192.168.10.102']
addresses = ['192.168.10.101']

clients = []
for address in addresses:
	client = LEDclient(address,PORT)
	clients.append(client)
	

counter = 0 
try:
	while True:
		for idx,client in enumerate(clients):
			datas=np.zeros((LED_COUNT,3))
			'''
			if counter % 2 ==0 :
				datas[:,0] = 255
			else:
				datas[:,2] = 255
			if False:
				datas[:,0] = int(127 * (np.sin(counter + np.radians(120.0) * idx) + 1 ))
				datas[:,1] = int(127 * (np.sin(counter + np.radians(120.0) + np.radians(120.0) * idx) + 1 )) # 255 * np.sin(counter + np.radians(120.0))
				datas[:,2] = int(127 * (np.sin(counter + np.radians(240.0)+ np.radians(120.0)* idx) + 1 ))  # 255 * np.sin(counter + np.radians(240.0))
							'''

			if True:
				datas[:,0] = int(127 * (np.sin(counter) + 1 ))
				datas[:,1] = int(127 * (np.sin(counter + np.radians(120.0) ) + 1 )) # 255 * np.sin(counter + np.radians(120.0))
				datas[:,2] = int(127 * (np.sin(counter + np.radians(240.0)) + 1 ))
			'''

			else:
				datas[:,0] = int(127 * (np.sin(counter + np.radians(120.0) * idx) + 1 ))
				datas[:,1] = int(127 * (np.sin(counter + np.radians(120.0) + np.radians(120.0) * idx) + 1 )) # 255 * np.sin(counter + np.radians(120.0))
				datas[:,2] = int(127 * (np.sin(counter + np.radians(240.0)+ np.radians(120.0)* idx) + 1 ))
				counter += .1
			'''

			client.send_data(datas)
			
		counter += .05
		#counter += 1
		print(counter, end='\r')
		time.sleep(0.1)

except KeyboardInterrupt:
		print("\nUser Interrupt")
		
except Exception as e:
	print("ERROR : ", e)

	