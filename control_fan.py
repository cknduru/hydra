import logger

MODULE = 'CONTROL_FAN'
state = 'off'

def toggle_fan():
	global state

	if state == 'off':
		state = 'on'
	else:
		state = 'off'

	logger.write(MODULE, 'toggling fan {}'.format(state))