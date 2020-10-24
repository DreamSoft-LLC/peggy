import random
import sys 
import os
from kivy.core.audio import SoundLoader
from tinytag import TinyTag

class MusicPlayer():
	def __init__(self,paths_=['C:\\Users\\Dethra_se\\Music']):
		self.paths_ = paths_
		self.player_ = SoundLoader()
		self.is_playing = False
		self.volume_ = 1
		self.current_music = ""
		self.index=None
		self.music_list = self.get_all_music()


	def get_all_music(self):
		music_list = []
		for path_x in self.paths_:
			for root, dirnames, filenames in os.walk(path_x):
				for nm in filenames:
					if os.path.splitext(nm)[1] == ".mp3":
						music_list.append([str(nm),str(os.path.join(root,nm))])
			return music_list

	def play_random(self):
		self.index = len(self.music_list)-1
		print(self.music_list[random.randint(0,self.index)][1])
		self.player_.load(str(self.music_list[random.randint(0,self.index)][1]))
		self.player_.play()
		self.is_playing = True

	def play(self,url):
		if self.is_playing:
			self.player_.stop()
			self.is_playing = False

		self.player_.load(str(url))
		self.player_.play()
		self.is_playing = False


	def pasue(self):
		if self.is_playing:
			self.player_.stop()
			self.is_playing = False


	def volume_up(self):
		pass

	def volume_down(self):
		pass
