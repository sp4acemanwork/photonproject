# import tkinter as tk

import os
# from tkinter import PhotoImage
from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
from customtkinter import CTkImage, CTkLabel
from player_screen import Test
splash_root = ctk.CTk()
splash_root.title("Photon Game")
splash_root.geometry("500x400")
splash_root.attributes("-fullscreen", True)


screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()


# Used os module to get the path of the image dynamically
image_path = os.path.join(os.path.dirname(__file__), "assets/images/logo.jpg")
image = Image.open(image_path)

photo = CTkImage(light_image=image, dark_image=image)
resized_image = CTkImage(light_image=image, size=(screen_width,screen_height))

image_label = CTkLabel(splash_root, image=resized_image, text="" )
image_label.pack(expand=True)

splash_root.bind("<Escape>", lambda e: splash_root.destroy())

def next_screen():
    Test()
    splash_root.destroy()
splash_root.after(3000, next_screen )
splash_root.mainloop()





