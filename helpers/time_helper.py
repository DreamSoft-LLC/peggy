from datetime import datetime, timedelta
import time as t
class Time():
	"""docstring for Time"""
	def __init__(self,speek):
		self.now = datetime.utcnow
		self.speek = speek
	def today(self):
		self.speek(self.now().date())

	def yesterday(self):
		self.speek(elf.now().date() - timedelta(days=1))

	def current_time(self):
		hour , min_ = map(int,t.strftime("%H %M").split())
		__xixa__ = "am"
		if hour > 12:
			hour = hour - 12
			__xixa__ = "pm"
		
		self.speek(f"{hour} : {min_} , {__xixa__}")

