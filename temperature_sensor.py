import logger as logger
import time

MODULE='SENSOR_TEMPERATURE'

q_in = None
q_out = None

# note that q_in / q_out are flipped compared to in main.py on purpose
def setup(q_out, q_in):
	time.sleep(4)
	q_out.append('{} {} {}'.format(MODULE, 2, 25.0))
	logger.write(MODULE, 'booted')