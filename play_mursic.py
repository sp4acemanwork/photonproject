#import pygame
import os

# pygame.mixer.init()
# if not pygame.mixer.get_init():
#     print("Pygame mixer did not initialize!")
# else:
#     try:
#         track_path = "/home/student/photonproject/music/photon_tracks/Track05.mp3"
#         if os.path.isfile(track_path):
#             pygame.mixer.music.set_volume(1.0)
#             print("Attempting to load track...")
#             pygame.mixer.music.load(track_path)
#             print("Track loaded. Attemtping to play...")
#             pygame.mixer.music.play()
#             print(f"Now playing: {os.path.basename(track_path)}")
#         else:
#             print("Track not found!")
#     except pygame.error as e:
#         print(f"Error loading or playing music: {e}")

import subprocess

# Path to your audio file
track_path = "/home/student/photonproject/music/photon_tracks/Track05.mp3"

try:
    # Use subprocess to call mpg123 and play the track
    subprocess.run(["mpg123", track_path])
    print(f"Now playing: {track_path}")
except Exception as e:
    print(f"Error playing music: {e}")

