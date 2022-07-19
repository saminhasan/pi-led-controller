from multiprocessing.connection import Client
import numpy as np
import time 
import sys

PORT = 1234
IP = '192.168.10.101'
LED_COUNT=48


class LEDclient:
	def __init__(self, ip, port, LED_COUNT=LED_COUNT):
		self.ip = ip
		self.port = port
		self.client = None
		self.connect()
	
	def connect(self):
		try:
			self.client = Client((self.ip, self.port))

		except Exception:
			print("Server Down")
			time.sleep(1)
			self.connect()
	
	def send_data(self, data):
		try:
			self.client.send(data)
			# print("Sent")

		except ConnectionResetError:
			print("Server shut down")
			self.connect()
			
	def close(self):
		data = np.zeros((LED_COUNT,3),dtype=int)
		client.send(data)
		client.close()
		
if __name__ == '__main__':
	client = LEDclient(IP, PORT)
	counter = 0
	datas=np.zeros((LED_COUNT,3))
	client.send_data(datas)
	time.sleep(1)
	while True:
		datas=np.zeros((LED_COUNT,3))

		#datas = np.random.randint(0,255, size=(LED_COUNT,3), dtype=np.uint32)
		#print(int(255 * np.sin(counter)))
		#datas[:,0] = int(127 * (np.sin(counter) + 1 ))
		#datas[:,1] = int(127 * (np.sin(counter + np.radians(120.0)) + 1 )) # 255 * np.sin(counter + np.radians(120.0))
		#datas[:,2] = int(127 * (np.sin(counter + np.radians(180.0)) + 1 ))  # 255 * np.sin(counter + np.radians(240.0))
		#counter += 0.785

		'''
		if counter < len(datas):
			datas[counter,0] = 255.0
			datas[counter,1] = 255.0
			datas[counter,2] = 255.0
		'''
		
		if counter % 2 ==0 :
			datas[:,0] = 255
		else:
			datas[:,2] = 255

		counter += 1

		client.send_data(datas)
		time.sleep(0.5)