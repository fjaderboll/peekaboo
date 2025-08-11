from buzzer import Buzzer
import random

class Sounds:
	def __init__(self, buzzer: Buzzer, mute: bool = False):
		self.buzzer = buzzer
		self.mute = mute
	
	def is_muted(self):
		return self.mute
	
	def set_mute(self, mute: bool):
		self.mute = mute
	
	def play_song(self, tones, tone_delay=0.3):
		if not self.mute:
			self.buzzer.play_song(tones, tone_delay=tone_delay)
	
	def play_random_sound(self, min_tones=2, max_tones=5):
		all_tones = list(self.buzzer.tones.keys())
		random_tones = []
		for _ in range(random.randint(min_tones, max_tones)):
			random_tone = random.choice(all_tones) # type: ignore
			random_tones.append(random_tone)
		#print(random_tones)
		self.play_song(random_tones, tone_delay=0.2)

	def play_startup(self):
		self.play_song(['G4', 'A4', 'B4', 'C5', 'D5'], tone_delay=0.1)

	def play_sleep(self):
		self.buzzer.play_song(['D5', 'C5', 'B4', 'A4', 'G4'], tone_delay=0.1)

	def play_found_someone(self):
		self.play_song(['D5', 'G4', 'D5', 'G4'], tone_delay=0.1)

	def play_lost_someone(self):
		self.play_song(['B4'], tone_delay=0.1)
	
	def play_startup_end(self):
		self.play_song(['C3', 'C5', 'P', 'C5'], tone_delay=0.1)
