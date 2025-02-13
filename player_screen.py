from customtkinter import *
from tkinter import *
import customtkinter

app = customtkinter.CTk()

app.geometry("500x400")
app.attributes("-zoomed", True)

set_appearance_mode("dark")

main_label = customtkinter.CTkLabel(app, width = 10, compound = "center", anchor = "center", text = "PHOTON", font = ('Roboto', 30))
l1 = Label(app, text = "Player ID")
l2 = Label(app, text = "Player Name")

main_label.grid(row = 0, column = 10)

red_team_label = customtkinter.CTkLabel(app, width = 10, text = "RED TEAM", font = ('Roboto', 20), text_color= "red")
green_team_label = customtkinter.CTkLabel(app, width = 10, text = "GREEN TEAM", font = ('Roboto', 20), text_color = "green")


red_team_label.grid(row = 1, column = 0)
green_team_label.grid(row = 1, column = 13)

l1.grid(row = 2, column = 1)
l2.grid(row = 2, column = 2)


#CODE FOR RED TEAM NAME, ID, #, AND TEXT BOXES 
#Code for which player # you are on red team

player_num_red = []
for i in range(15):
    player_num_red.append(CTkTextbox(app, width = 40, height = 10, border_width = 2, border_color = "red"))

num_row = 3
for item in player_num_red:
    item.insert(index = "0.0", text = num_row - 2)
    item.configure(state = "disabled")
    item.grid(row = num_row, column = 0, pady = 2)
    num_row += 1

#code for text box that can have an id input for red team

player_id = []

for i in range(15):
    player_id.append(Entry(app))

player_id_row = 3

for item in player_id:
    item.grid(row = player_id_row, column = 1, pady = 2)
    player_id_row += 1


#code for player to put in their player name on read team

player_name = []

for i in range(15):
    player_name.append(Entry(app))

player_name_row = 3

for item in player_name:
    item.grid(row = player_name_row, column = 2, padx = 2,pady = 2)
    player_name_row += 1








app.mainloop()