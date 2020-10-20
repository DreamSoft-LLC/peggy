import pyttsx3
import random
import speech_recognition as sr
from config import AI_NAME, VERSION, ERRORS, SHUTDOWN_PHRASE
from reg.boot import  CALL_REG ,CALL_RESPONSE

class Peggy():
	"""docstring for Peggy"""
	def __init__(self, version="0.0.1"):
		self.version = version
		self.name = "peggy"
		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty('voices') 

	def speek(self,text):
		self.engine.setProperty('voice', self.voices[1].id) 
		self.engine.setProperty('rate', 120)
		self.engine.say(text)
		self.engine.runAndWait()

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

	def run(self):
		while True:
		 	text = self.listen()
		 	text = SHUTDOWN_PHRASE

		 	for res in CALL_REG:
		 		if text == res:
		 			self.speek(random.ranint(0,len(CALL_RESPONSE)-1))
		 			# option to chose without calling peggy again
		 			text = self.listen()
		 			break
		 		else:
		 			# looping through the partttens
		 			pass

		 	if text in ERRORS or text == None:
		 		break

		 	if text == SHUTDOWN_PHRASE:
		 		self.speek("Shutting Down")
		 		break
		 		
		