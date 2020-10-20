from datetime import datetime ,timedelta
import time
from playsound import playsound

class Alarm():
	"""docstring for Alarm"""
	def __init__(self, alarms=[]):
		self.alarms = alarms

	def set_alarm(self,time,date_=datetime.utcnow().date()):
		response = ""
		if(len(self.alarm)):
			for alarm in self.alarms:
				if alarm[0] == time and alarm[1] ==date_:
					response = "Alarm already set"
				else:
					self.alarms.append([time , date_])
					response = "Alarm set"
		else:
			self.alarms.append([time , date_])
			response = "Alarm set"

		return response

	def run(self):
		time.sleep(10)
		if(len(self.alarms)):
			while True:
				now = datetime.utcnow()
				alarm_index=0;
				for alarm in self.alarms:
					if alarm[0] == f"{now.minute} : {now.hour}" and alarm[1] == datetime.utcnow().date():
						# play sound
						playsound('/path/to/a/sound/file/you/want/to/play.mp3')
						time.sleep(1000)
						playsound('/path/to/a/sound/file/you/want/to/play.mp3')
						time.sleep(1000)
						playsound('/path/to/a/sound/file/you/want/to/play.mp3')
						# remove item from 
						self.alarms.remove(alarm)


