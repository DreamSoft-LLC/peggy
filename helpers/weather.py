import requests
import geocoder
import json

class Weather():
	"""docstring for Weather"""
	def __init__(self, api_key="cb261bd63a067e90ebce0fe0c36b4c4a"):
		self.api_key = api_key
		self.latlon = ['lat','lon'] #self.get_latlon()
		self.url = f"api.openweathermap.org/data/2.5/weather?lat={self.latlon[0]}&lon={self.latlon[1]}&appid={self.api_key}"
		
	def get_latlon(self):
		try:
			g = geocoder.ip('me')
			return g.latlng
		except Exception as e:
			return ['lat','lon']
		

	def get_current_wether(self):
		response = requests.get(url)
		return json.loads(response.text)
		
	def get_current_temperature(self):

		pass
	def weather_response_eng(self,disc,temp):
		return f"Just some {disc} in the skies today. The temperaure outside is going to be {temp} celcius"

