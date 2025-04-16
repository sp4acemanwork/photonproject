import os
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
import subprocess
import pygame
import os
import random
from window import window

class CountdownTimer:
    def __init__(self, parent: window, callback):  # fixed parent to be window
        self.parent = parent.window
        self.callback = callback
        self.countdown_window = Toplevel(self.parent)
        self.countdown_window.title("Game Countdown")
        self.countdown_window.geometry("800x600")
        self.countdown_window.attributes("-fullscreen", True)
        #pygame.mixer is a module for loading and playing sounds with the GUI 
        pygame.mixer.init()

        screen_width = self.countdown_window.winfo_screenwidth()
        screen_height = self.countdown_window.winfo_screenheight()

        # Load background image
        background_path = os.path.join(os.path.dirname(__file__), "countdown_images/background.tif")
        background_image = Image.open(background_path)
        background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
        background_photo = ImageTk.PhotoImage(background_image)

        # Create background label
        background_label = Label(self.countdown_window, image=background_photo, borderwidth=0, highlightthickness=0) # Removes the white border
        background_label.image = background_photo  # Keep a reference to avoid garbage collection
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.countdown_images = [f"{i}.tif" for i in range(30, -1, -1)]
        self.countdown_folder = os.path.join(os.path.dirname(__file__), "countdown_images")

        self.music_folder = os.path.join(os.path.dirname(__file__), "music/photon_tracks")  # Dynamically locate the music folder

        self.countdown_label = Label(self.countdown_window, borderwidth=0, highlightthickness=0) # Removes the white border
        self.countdown_label.place(relx=0.501, rely=0.582, anchor=CENTER)

        self.countdown_window.bind("<Escape>", lambda e: self.countdown_window.destroy())
        self.countdown_window.bind("<F1>", lambda e: self.countdown_window.minsize())
        self.show_image(0)

    def show_image(self, index):
        if index < len(self.countdown_images):
            # Will start audio track when countdown is 18 seconds left
            if index == 15:
                # Select a random track from the music folder
                tracks = [f for f in os.listdir(self.music_folder) if f.endswith(".mp3")]
                if not tracks:
                    print("No music tracks found.")
                    return
                track_path = os.path.join(self.music_folder, random.choice(tracks))
                try:
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.load(track_path)
                    pygame.mixer.music.play()
                    print(f"Now playing: {os.path.basename(track_path)}")
                except pygame.error as e:
                    print(f"Error Loading or Playing Music: {e}")
            image_path = os.path.join(self.countdown_folder, self.countdown_images[index])
            image = Image.open(image_path)
            # Resize the number images
            number_width = 805  # Set the desired width
            number_height = 270  # Set the desired height
            image = image.resize((number_width, number_height), Image.LANCZOS)
            
            photo = ImageTk.PhotoImage(image)
            self.countdown_label.lift()  # Ensure the countdown label is in front
            self.countdown_label.config(image=photo)
            self.countdown_label.image = photo
            if index <= 24:
                self.countdown_window.after(1000, self.show_image, index + 1)
            else:
                self.countdown_window.after(1500, self.show_image, index + 1)
        else:
            self.countdown_window.destroy()
            self.callback()  # Trigger the callback to start the next action
