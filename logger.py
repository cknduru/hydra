def write(module, msg):
	flog = open('log.txt', 'a')
	log_message = '[*] {}: {}'.format(module, msg)

	print(log_message)
	flog.write(log_message + '\n')
	flog.close()

def setup():
	flog = open('log.txt', 'w')
	flog.write('')