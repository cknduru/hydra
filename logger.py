def write(module, msg):
	flog = open('log.txt', 'a')
	log_message = '[*] {}: {}'.format(module, msg)

	flog.write(log_message + '\n')
	flog.close()

def write_e(module, msg):
	flog = open('log.txt', 'a')
	log_message = '[/] {}: {}'.format(module, msg)

	flog.write(log_message + '\n')
	flog.close()

def write_m(module, sensor_num, reading):
	flog = open('log.txt', 'a')
	log_message = '[*] {}: sensor_num = {}, reading = {}'.format(module, sensor_num, reading)

	flog.write(log_message + '\n')
	flog.close()

def setup():
	flog = open('log.txt', 'w')
	flog.write('')