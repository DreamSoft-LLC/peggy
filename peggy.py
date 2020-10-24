import os 
import sys
import random
import threading
import re
import requests
import pyttsx3
from datetime import datetime
import speech_recognition as sr
from word2number import w2n

from helpers.alarms import Alarm
from helpers.time_helper import Time as TimeHelper
from helpers.weather import Weather
from subs.limeplayer import MusicPlayer

from config import AI_NAME, VERSION, ERRORS, SHUTDOWN_PHRASE
from reg.boot import  CALL_REG ,CALL_RESPONSE , TAGS,BASIC_COMMAND

class AlarmModule():
	"""docstring for AlarmModule"""
	def __init__(self,speek,listen, alarm=Alarm(alarms=[])):
		self.alarm = alarm
		self.listen = listen
		self.speek = speek
		threading.Thread(target=self.alarm.run).start()

	def set_alarm(self):
		self.speek("what time do you need the alarm to ring ?")
		text = self.listen()
		text = "ten twenty-five"
		if text:
			text = text.lower().split(" ")
			ttime_ = f"{w2n.word_to_num(text[0])}:{w2n.word_to_num(text[1])}"
			self.alarm.set_alarm(ttime_)
			print(self.alarm.alarms)

	def show_alarms(self):
		self.speek(f"You currrenly have {len(self.alarm.alarms)} set alarm.")
		counter = 0
		for t,d in self.alarm.alarms:
			print(t,str(d))
			self.speek(f"alarm number {counter+1} is set to {t} .")
			counter +=1

	def is_mute_alarm(self):
		if(self.alarm.mute_state()):
			self.speek(f"Your alarm is currently in silent mode.")
		else:
			self.speek(f"Your alarm is currently in loud mode.")

	def remove_alarm(self,num):
		self.alarm.alarms.remove(self.alarm.alarms[int(num)-1])
		self.speek(f"Alarm has been removed.")

	def remove_alarms(self):
		self.alarm.alarms = []
		self.speek(f"all set alarms have been removed.")

	def mute_alarm(self):
		self.alarm.mute = True
		self.speek(f"Alarm muted.")

	def un_mute_alarm(self):
		self.alarm.mute = False
		self.speek(f"Alarm has been unmuted.")

class Peggy():
	"""docstring for Peggy"""
	def __init__(self, version="0.0.1"):
		self.version = version
		self.name = "peggy"
		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty('voices') 
		# instantiating modules
		self.alarm_module = AlarmModule(self.speek,self.listen)
		self.time_helper = TimeHelper(self.speek)
		self.weather = Weather()
		self.music_player = MusicPlayer()
		# module index fun acuracy
		self.TAG_INDEX_MODULE = [self.alarm_module,self.time_helper,self.music_player]

	def speek(self,text):
		self.engine.setProperty('voice', self.voices[1].id) 
		self.engine.setProperty('rate', 120)
		self.engine.say(text)
		self.engine.runAndWait()

	def check_connection():
		try:
			requests.get("https://google.com")
			return 1
		except Exception as e:
			return 0

	def listen(self):
		r = sr.Recognizer()
		try:
			with sr.Microphone() as source:
				audio = r.listen(source)
				said = ""

				try:
					said = r.recognize_gogle(audio)
				except Exception as e:
					print(e)

				return said.lower()
		except OSError:
			self.speek("Sorry! Your device Microphone is not configured properly.")

		except Exception as e:
			print(e)

	def run_once(self):
		text = self.listen()
		pass

	def run(self):
		while True:
		 	text = self.listen()
		 	text = "hey peggy"

		 	for res in CALL_REG:
		 		if text == res:
		 			self.speek(CALL_RESPONSE[random.randint(0,len(CALL_RESPONSE)-1)])
		 			# option to chose without calling peggy again
		 			text = self.listen()
		 			text = "set alarm"
		 			for tag , num in TAGS.items():
		 				if tag in text:
		 					print(tag,num)
		 					for parten,func_ in BASIC_COMMAND[num].items():
		 						if parten.match(text):
		 							print(parten)
		 							func_(self.TAG_INDEX_MODULE[num])()
		 							break
		 				break
		 		else:
		 			# looping through the partttens
		 			pass

		 	if text in ERRORS or text == None:
		 		break

		 	if text == SHUTDOWN_PHRASE:
		 		self.speek("Shutting Down")
		 		a=AlarmModule()
		 		a.set_alarm()
		 		break
		 		
		
