from buzzer import Buzzer
import random

buzzer = Buzzer(18)

# song
song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]
buzzer.play_song(song)

# random tones
min_msg_len = 2
max_msg_len = 5
random_tones = []
for _ in range(random.randint(min_msg_len, max_msg_len)):
	random_tone = random.choice(list(buzzer.tones.keys()))
	random_tones.append(random_tone)
print(random_tones)
buzzer.play_song(random_tones, tone_delay=0.2)
