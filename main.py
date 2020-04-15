import logger as logger
import temperature_sensor as ts
MODULE = 'MAIN'

if __name__=='__main__':
	logger.setup()
	ts.setup()
	logger.write(MODULE, 'booted')