from buzzer import Buzzer
from buzzer_sounds import Sounds
import time

buzzer = Buzzer(18)
sounds = Sounds(buzzer)

print("Startup")
sounds.play_startup()
time.sleep(1)

print("Found someone")
sounds.play_found_someone()
time.sleep(1)

print("Lost someone")
sounds.play_lost_someone()
time.sleep(1)

print("Random sound")
sounds.play_random_sound()
time.sleep(1)

print("Play a song")
song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]
buzzer.play_song(song)
