from datetime import datetime ,timedelta
import time
from playsound import playsound
import threading
class Alarm():
	"""docstring for Alarm"""
	def __init__(self, alarms=[],mute=False):
		self.alarms = alarms
		self.mute=mute

	def set_alarm(self,time,date_=datetime.utcnow().date()):
		response = ""
		if(len(self.alarms)):
			for alarm in self.alarms:
				if alarm[0] == time and alarm[1] ==date_:
					response = "Alarm already set"
				else:
					self.alarms.append([time , date_])
					response = "Alarm set"
		else:
			self.alarms.append([(time) , date_])
			print(time,date_)
			response = "Alarm set"
			threading.Thread(target=self.run()).start()
			

		return response

	def mute_alarm(self):
		self.mute = True
		return mute

	def un_mute_alarm(self):
		self.mute = False
		return mute

	def mute_state(self):
		return self.mute

	def run(self):
		time.sleep(10)
		if len(self.alarms):
			while True:
				hour , min_ = map(int,time.strftime("%H %M").split())
				alarm_index=0;
				__cix__ = "am"

				if hour > 12 :
					hour = hour-12
					__cix__ = "pm"
					
				print(f"{hour} : {min_} {__cix__}")
				for alarm in self.alarms:
					print(alarm[0] , f"{hour}:{min_}")
					print(alarm[0] == f"{hour}:{min_}")
					if alarm[0] == f"{hour}:{min_}" and alarm[1] == datetime.utcnow().date():
						print(f"alarm {alarm[0]} is ringing")
						# play sound
						if self.mute == False:
							try:
								playsound('C:\\Users\\Dethra_se\\Desktop\\PROJECTS\\peggy\\helpers\\alarm.wav')
							except Exception as e:
								print("beep")
							time.sleep(1000)
							try:
								playsound('C:\\Users\\Dethra_se\\Desktop\\PROJECTS\\peggy\\helpers\\alarm.wav')
							except Exception as e:
								print("beep")
							time.sleep(1000)
							try:
								playsound('C:\\Users\\Dethra_se\\Desktop\\PROJECTS\\peggy\\helpers\\alarm.wav')
							except Exception as e:
								print("beep")
						# remove item from 
						self.alarms.remove(alarm)
				if len(self.alarms) == 0:
					break


