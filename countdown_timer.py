import os
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk

class CountdownTimer:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        self.countdown_window = Toplevel(self.parent)
        self.countdown_window.title("Game Countdown")
        self.countdown_window.geometry("800x600")
        self.countdown_window.attributes("-fullscreen", True)

        screen_width = self.countdown_window.winfo_screenwidth()
        screen_height = self.countdown_window.winfo_screenheight()

        # Load background image
        background_path = os.path.join(os.path.dirname(__file__), "countdown_images/background.tif")
        background_image = Image.open(background_path)
        background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
        background_photo = ImageTk.PhotoImage(background_image)

        # Create background label
        background_label = Label(self.countdown_window, image=background_photo)
        background_label.image = background_photo  # Keep a reference to avoid garbage collection
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.countdown_images = [f"{i}.tif" for i in range(30, -1, -1)]
        self.countdown_folder = os.path.join(os.path.dirname(__file__), "countdown_images")

        self.countdown_label = Label(self.countdown_window)
        self.countdown_label.place(relx=0.501, rely=0.583, anchor=CENTER)

        self.countdown_window.bind("<Escape>", lambda e: self.countdown_window.destroy())

        self.show_image(0)

    def show_image(self, index):
        if index < len(self.countdown_images):
            image_path = os.path.join(self.countdown_folder, self.countdown_images[index])
            image = Image.open(image_path)
            
            # Resize the number images
            number_width = 795  # Set the desired width
            number_height = 270  # Set the desired height
            image = image.resize((number_width, number_height), Image.LANCZOS)
            
            photo = ImageTk.PhotoImage(image)
            self.countdown_label.lift()  # Ensure the countdown label is in front
            self.countdown_label.config(image=photo)
            self.countdown_label.image = photo
            self.countdown_window.after(1000, self.show_image, index + 1)
        else:
            self.countdown_window.destroy()
            self.callback()
