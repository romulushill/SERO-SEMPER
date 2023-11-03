from termcolor import colored
from datetime import datetime


class log:
	def __init__(self):
		self.ready = False
		self.ready = True

	def console(self, content=None, ctype=1):
		current_datetime = datetime.now()
		formatted_date = current_datetime.strftime("%Y-%m-%d")
		try:
			if self.ready:
				if content != None:
					if ctype == 1:
						value = colored(content, 'green')
					elif ctype == 2:
						value = colored(content, 'yellow')
					elif ctype == 3:
						value = colored(content, 'red')
					else:
						value = colored(content, 'blue')
					print(value)
					return True
				else:
					return False
			else:
				return False
		except:
			print("FATAL ERROR")
			return False
