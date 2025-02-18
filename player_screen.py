from customtkinter import *
from tkinter import *
import customtkinter
from server import handler

class Test:
    def __init__(self):

        
        self.game_handler = handler("127.0.0.1", 7502, 7504, 1024)
        self.game_handler.start_game()

        self.num_players = 0
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
           
            for item in range(15):

                new_id = player_id[item].get()
                # print("Entry value:", new_id)
                new_name = player_name[item].get()
                temp_tuple = (new_id, new_name)
                if temp_tuple not in list_of_id_and_names:
                    list_of_id_and_names.append((new_id, new_name))
            

            for i in list_of_id_and_names:
                if i[0] == '' and i[1] == '':
                    list_of_id_and_names.pop(list_of_id_and_names.index(i))
                else:
                    self.game_handler.add_player(i[1],i[0],i[0])

            # print(f"Updated list of names and ids: {list_of_id_and_names}")
            
            

        add_values = customtkinter.CTkButton(app, text="Confirm Info", command = get_entry_value)
        add_values.grid(row = 2, column = 11)

        change_network_button = customtkinter.CTkButton(app, text="Change Network", command=self.change_network)
        change_network_button.grid(row=20, column=10, pady=20, columnspan=3)

        app.mainloop()

    def change_network(self):
        # Create a new window to enter network details
        network_window = Toplevel()
        network_window.title("Change Network")
        network_window.geometry("300x200")

        Label(network_window, text="New IP:").pack(pady=5)
        ip_entry = Entry(network_window)
        ip_entry.pack(pady=5)

        Label(network_window, text="New Port:").pack(pady=5)
        port_entry = Entry(network_window)
        port_entry.pack(pady=5)

        def submit_network():
            new_ip = ip_entry.get()
            new_port = int(port_entry.get())
            if not new_port:
                new_port = self.game_handler.local_port_send
            
            print(f"Changing network to IP: {new_ip}, Port: {new_port}")
            self.game_handler.change_socket(new_ip, new_port)
            network_window.destroy()

        submit_button = customtkinter.CTkButton(network_window, text="Submit", command=submit_network)
        submit_button.pack(pady=20)
