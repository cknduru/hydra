import logger as logger
from threading import Thread
import time
import sys

import temperature_sensor as ts
import control_fan as cf

MODULE = 'MAIN'
READ_TIMEOUT = 2

def handle_reading(reading):
	# split reading into tuple
	rsplit = reading.split(' ')
	module = rsplit[0]
	sensor_num = rsplit[1]
	reading = rsplit[2]

	logger.write_m(module, sensor_num, reading)

	# direct message to correct consumer
	if module == 'SENSOR_TEMPERATURE':
		cf.toggle_fan()

def start_services(q_in, q_out):
	try:
		Thread(target=ts.setup, args=(q_in, q_out)).start()
	except Exception as ex:
		logger.write_e(MODULE, "unable to start thread")
		sys.exit(-1)

if __name__=='__main__':
	logger.setup()

	q_in = []
	q_out = []

	start_services(q_in, q_out)
	logger.write(MODULE, 'booted')

	while True:
		try:
			msg = q_in.pop(0)
			handle_reading(msg)
			time.sleep(READ_TIMEOUT)
		except:
			# no readings
			pass