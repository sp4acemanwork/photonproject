import os
from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
from customtkinter import CTkImage, CTkLabel
from player_screen import PlayerScreen

splash_root = ctk.CTk()
splash_root.title("Photon Game")
splash_root.geometry("500x400")
splash_root.attributes("-fullscreen", True)

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

# Used os module to get the path of the image dynamically
image_path = os.path.join(os.path.dirname(__file__), "assets/images/logo.jpg")
image = Image.open(image_path)

resized_image = CTkImage(light_image=image, size=(screen_width, screen_height))

image_label = CTkLabel(splash_root, image=resized_image, text="")
image_label.pack(expand=True)

splash_root.bind("<Escape>", lambda e: splash_root.destroy())

def next_screen():
    splash_root.destroy()
    player_screen = PlayerScreen()
    player_screen.main()

splash_root.after(3000, next_screen)
splash_root.mainloop()