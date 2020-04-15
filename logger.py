from time import localtime, strftime

def get_time():
	return str(strftime("%d-%m-%Y %H:%M:%S", localtime()))

def write(module, msg):
	flog = open('log.txt', 'a')
	log_message = '[*] {} {}: {}'.format(get_time(), module, msg)

	flog.write(log_message + '\n')
	flog.close()

def write_e(module, msg):
	flog = open('log.txt', 'a')
	log_message = '[/] {} {}: {}'.format(get_time(), module, msg)

	flog.write(log_message + '\n')
	flog.close()

def write_m(module, sensor_num, reading):
	flog = open('log.txt', 'a')
	log_message = '[*] {} {}: sensor_num = {}, reading = {}'.format(get_time(), module, sensor_num, reading)

	flog.write(log_message + '\n')
	flog.close()

def setup():
	# overwrite file on each start
	flog = open('log.txt', 'w')
	flog.write('')