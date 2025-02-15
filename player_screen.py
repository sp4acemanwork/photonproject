from customtkinter import *
from tkinter import *
import customtkinter


class Test:
    def __init__(self):
        

        app = customtkinter.CTk()

        app.geometry("500x400")
        app.attributes("-zoomed", True)

        set_appearance_mode("dark")

        main_label = customtkinter.CTkLabel(app, width = 10, compound = "center", anchor = "center", text = "PHOTON", font = ('Roboto', 30))
        l1_red = Label(app, text = "Player ID")
        l2_red = Label(app, text = "Player Name")
        l1_green = Label(app, text = "Player ID")
        l2_green = Label(app, text = "Player Name")

        main_label.grid(row = 0, column = 10)

        red_team_label = customtkinter.CTkLabel(app, width = 10, text = "RED TEAM", font = ('Roboto', 20), text_color= "red")
        green_team_label = customtkinter.CTkLabel(app, width = 10, text = "GREEN TEAM", font = ('Roboto', 20), text_color = "green")




        red_team_label.grid(row = 1, column = 0)
        green_team_label.grid(row = 1, column = 12)

        l1_red.grid(row = 2, column = 1)
        l2_red.grid(row = 2, column = 2)
        l1_green.grid(row = 2, column = 13)
        l2_green.grid(row = 2, column = 14)



        #CODE FOR GREEN TEAM NAME, ID, # AND TEXT BOXES
        #Code for which player # you are on the green team
        player_num_green = []
        for i in range(15):
            player_num_green.append(CTkTextbox(app, width = 40, height = 10, border_width = 2, border_color = "green"))

        green_num_row = 3


        for item in player_num_green:
            item.insert(index = "0.0", text = green_num_row - 2)
            item.configure(state = "disabled")
            item.grid(row = green_num_row, column = 12, pady = 2)
            green_num_row += 1

        #code for text box that can have an id input for green team
        green_player_id = []

        transmitting_id_green = []

        for i in range(15):
            green_player_id.append(Entry(app))

            

        player_id_row = 3

        for item in green_player_id:
            item.grid(row = player_id_row, column = 13, pady = 2)
            player_id_row += 1


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


        #code for text box that can have a name input for green team
        green_player_name = []

        for i in range(15):
            green_player_name.append(Entry(app))

        player_name_row = 3

        for item in green_player_name:
            item.grid(row = player_name_row, column = 14, padx = 2,pady = 2)
            player_name_row += 1





        #red team random generated IDs
        transmitting_ids_red = []

        #code for text box that can have an id input for red team
        player_id = []

        for item  in range(15):

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


        list_of_id_and_names = []

        def get_entry_value():
            for item in range(2):
                new_id = player_id[item].get()
                print("Entry value:", new_id)
                new_name = player_name[item].get()
                list_of_id_and_names.append((new_id, new_name))
            print(f"this is the list of tuples needed: {list_of_id_and_names}")

        add_values = customtkinter.CTkButton(app, text="Confirm Info", command = get_entry_value)
        add_values.grid(row = 2, column = 11)




                






        app.mainloop()