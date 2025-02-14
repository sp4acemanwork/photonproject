# import tkinter as tk
# from tkinter import PhotoImage
from tkinter import *
from PIL import ImageTk, Image
import customtkinter




splash_root = customtkinter.CTk()
splash_root.title("Photon Game")
splash_root.iconbitmap('c:/Users/Tonyo/software/splash_icon.ico')

splash_root.state('zoomed')

# splash_label = Label(splash_root, )


#image = PhotoImage(file="splash_screen.png")
#image_label = tkinter.Label(splash_root, image = image)
#image_label.pack()

#Create our image 
photon = Image.open("c:/Users/Tonyo/software/splash_screen.png").resize((600,400))
photon = ImageTk.PhotoImage(photon)

#Create Label
photon_label = Label(splash_root, image=photon)
photon_label.pack(pady=20)

def player_screen():
    player_window = Tk()
    #splash_root.destroy()
    player_window.title("Main Window - Player Screen")
    splash_root.iconbitmap('c:/Users/Tonyo/software/splash_icon.ico')
    player_window.geometry("500x550")

splash_root.after(3000, player_screen)
mainloop()