from customtkinter import *
from tkinter import *
import customtkinter
from server import handler
import os
from PIL import Image, ImageTk
from countdown_timer import CountdownTimer
from window import actionFrame, actionFrame2
from window import window
import pygame 
import random

class PlayerScreen:
    def __init__(self):
        self.game_handler = handler("127.0.0.1", 7501, 1024)
        self.app = customtkinter.CTk()
        self.app.geometry("500x400")
        self.app.attributes("-zoomed", True)
        set_appearance_mode("dark")
        self.app.bind("<Return>", lambda e: self.get_entry_value())
        self.app.bind("<F5>", lambda e: self.start_game_with_countdown())
        self.app.bind("<F12>", lambda e: self.delete_entries())        
        self.teams_data = {}

    def create(self, col: int, team_name: str, team_color: str):
        # creates the labels
        main_label = customtkinter.CTkLabel(self.app, width = 10, compound = "center", anchor = "center", text = "PHOTON", font = ('Roboto', 30))
        player_id = Label(self.app, text = "Player ID")
        equipment_id = Label(self.app, text = "Equipment ID")
        player_name = Label(self.app, text = "Player Name")
        team_label = customtkinter.CTkLabel(self.app, width = 10, text = team_name, font = ('Roboto', 20), text_color= team_color)

        # writes the grid
        main_label.grid(row = 0, column = 10)
        team_label.grid(row = 1, column = col)
        player_id.grid(row = 2, column = col + 1)
        equipment_id.grid(row=2,column = col + 2)
        player_name.grid(row = 2, column = col + 3)
        
        # creates the player numbers
        player_num = []
        for i in range(15):
            player_num.append(CTkTextbox(self.app, width = 40, height = 10, border_width = 2, border_color = team_color))
        num_row = 3
        for item in player_num:
            item.insert(index = "0.0", text = num_row - 2)
            item.configure(state = "disabled")
            item.grid(row = num_row, column = col, pady = 2)
            num_row += 1

        # ceates entry fields for IDs and Names
        self.teams_data[team_name] = {"player_ids": [],"equpiment_ids": [], "player_names": []}
        for i in range(15):
            id_entry = Entry(self.app)
            equipment_id_entry = Entry(self.app)
            name_entry = Entry(self.app)

            id_entry.grid(row=3 + i, column=col + 1, pady=2)
            equipment_id_entry.grid(row=3 + i, column=col + 2, padx=2, pady=2)
            name_entry.grid(row=3 + i, column=col + 3, padx=2, pady=2)

            self.teams_data[team_name]["player_ids"].append(id_entry)
            self.teams_data[team_name]["equpiment_ids"].append(equipment_id_entry)
            self.teams_data[team_name]["player_names"].append(name_entry)

            
    def delete_entries(self):
        for team, data in self.teams_data.items():
            for id_entry, eqid_entry, name_entry in zip(data["player_ids"], data["equpiment_ids"], data["player_names"]):
                id_entry.delete(0, END)
                eqid_entry.delete(0, END)
                name_entry.delete(0, END)

    def get_entry_value(self):
        self.list_of_id_and_names = []

        for team, data in self.teams_data.items():
            for  id_entry,eqid_entry, name_entry in zip(data["player_ids"],data["equpiment_ids"], data["player_names"]):
                new_id = id_entry.get()
                new_eqid = eqid_entry.get()
                new_name = name_entry.get()

                if new_id or new_name or new_eqid:  # Ignore empty entries
                    self.list_of_id_and_names.append((new_id, new_eqid, new_name, team))
                    self.game_handler.add_player(new_name, new_id, new_eqid)

        print(self.list_of_id_and_names)
        
    def buttons(self):
        # To modify Confirm Info button
        add_values = customtkinter.CTkButton(self.app, text="Confirm Info", command=self.get_entry_value)
        add_values.grid(row=2, column=11)

        # To modify Start button
        start_button = customtkinter.CTkButton(self.app, text="<F5> Start", command=self.start_game_with_countdown)
        start_button.grid(row=20, column=11, pady=20, columnspan=1)

        # To modify Change Network button
        change_network_button = customtkinter.CTkButton(self.app, text="Change Network", command=self.change_network)
        change_network_button.grid(row=20, column=10, pady=20, columnspan=1)

        # To modify Delete Entries button
        delete_all_entries = customtkinter.CTkButton(self.app, text="<F12> Delete Entries", command=self.delete_entries)
        delete_all_entries.grid(row=20, column=12, pady=20, columnspan=1)

    def start_game(self):
        self.game_handler.start_game()
        folder = "/home/student/photonproject/music/photon_tracks"
        self.play_music(folder)


    def start_game_with_countdown(self):
        CountdownTimer(self.app, self.countdown_to_playaction(self.countdown_seconds))
        
    

    def countdown_to_playaction(self, total_time):
        self.app.destroy()
        print("Countdown finished, switching to ActionFrame screen...")
        #New window initialized 
        test = window()
        testpage = actionFrame(test.window, test)
        testpage2 = actionFrame2(test.window, test)
        test.addPage("actionscreen", testpage)
        
        test.addPage("test", testpage2)
        test.redraw("actionscreen")
        list_of_players = self.game_handler.database_handler.get_all_players()
        testpage.append_list(self.list_of_id_and_names)

    def pick_random_file(self, folder_path):
        if not os.path.isdir(folder_path):
            return None
        files = os.listdir(folder_path)
        if not files:
            return None
        random_file = random.choice(files)
        return os.path.join(folder_path, random_file)

    def play_music(self, folder_path):
        track_path = self.pick_random_file(folder_path)

        if not track_path:
            print("File not Found.")
            return
        
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()



    def change_network(self):
        # Create a new window to enter network details
        network_window = Toplevel()
        network_window.title("Change Network")
        network_window.geometry("300x150")

        # Center the pop-up window
        window_width = 300
        window_height = 150
        screen_width = network_window.winfo_screenwidth()
        screen_height = network_window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        network_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        Label(network_window, text="New IP:").pack(pady=5)
        ip_entry = Entry(network_window)
        ip_entry.pack(pady=5)

        def submit_network():
            new_ip = ip_entry.get()
            print(f"Changing network to IP: {new_ip}")
            self.game_handler.change_socket(new_ip, self.game_handler.local_port_send)
            network_window.destroy()

        submit_button = customtkinter.CTkButton(network_window, text="Submit", command=submit_network)
        submit_button.pack(pady=20)

    def main(self):
        self.create(0, "RED TEAM", "red")
        self.create(12, "GREEN TEAM", "green")
        self.buttons()
        self.app.mainloop()
