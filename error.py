import colorama, os
from time import sleep as delay

pref = os.environ.get('logging')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class set:
	def error(msg,code):
		print(bcolors.FAIL+msg+bcolors.ENDC)
		delay(1)
		raise RuntimeError(msg)
	def warning(msg):
		if os.environ.get('logging') == "on":
			print(bcolors.WARNING+msg+bcolors.ENDC)

	def log(msg):
		if os.environ.get('logging') == "on":
			print(msg)