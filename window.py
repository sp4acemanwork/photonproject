import tkinter as tk
import random
from server import handler
from PIL import Image, ImageTk
import os
from server import usr
game_handler = handler("127.0.0.1", 7502, 1024)
# import keyboard # implement later


class window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.attributes("-fullscreen", True)
        self.currentwindow = None
        self.pages = {}

    def addPage(self, name: str, el: 'page'):
        print
        self.pages[name] = el
        print(self.pages)

    def redraw_intital(self, windowname: str):  # initial redraw requires page to be declared
        print("packpages")

        page = self.pages[windowname]
        self.currentwindow = windowname
        for element in page.page_elements.values():  # Access the page elements
            element["el"].pack(**element["opt"])  # Pack each element
            print(f"packing{0} ", element)

    def redraw(self):  # otherwise redraw current page
        print("packpages")
        page = self.currentwindow
        for element in page.page_elements.values():  # Access the page elements
            element["el"].pack(**element["opt"])  # Pack each element
            print(f"packing{0} ", element)

    def hidepage(self):
        if not self.currentwindow:
            return

        current_page = self.currentwindow
        page = self.pages.get(current_page)
        if page:
            for element in page.page_elements.values():  # Access the page elements
                element["el"].pack_forget()  # Pack each element
                print(f"unpacking{0} ", element)

    def switch_window(self, windowname: str):
        print(f"switching to window {0}", windowname)
        print(self.pages)
        self.hidepage()
        self.redraw_intital(windowname)


class page:
    def __init__(self, parent: window):
        self.parrent_window = parent.window
        self.parent = parent
        self.page_elements = {}
        self.setvis = True


class actionFrame(page):  # example of how a page could be implemented
    def __init__(self,parent: window):  # could horribly backfire
        super().__init__(parent)
        self.parent = parent
        self.window = parent.window
        self.buttonfunc = lambda: self.parent.switch_window("test")  # set function that button will call here or set it with the function setbuttonfunction(func)
        self.page_elements = {
            "redteam_frame": {"el": tk.Frame(self.window, bg="red", width=60), "opt": {"fill": "both", "side": "right", "expand": False}},
            "greenteam_frame": {"el": tk.Frame(self.window, bg="green", width=60), "opt": {"fill": "both", "side": "left", "expand": False}},
            "stylized_b_green": {"el": tk.Frame(self.window, bg="brown", width = 20), "opt": {"fill": "both", "side": "left", "expand": False}},
            "split_frame": {"el": tk.Frame(self.window, bg="black"), "opt": {"fill": "both", "side": "left", "expand": True}},
            "stylized_b_red": {"el": tk.Frame(self.window, bg="brown", width = 20), "opt": {"fill": "both", "side": "right", "expand": False}}
        }
        self.middle = {"button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="back", command=self.buttonfunc), "opt": {}}}
        # stupid dumb fix because we didn't use html and typescript

        lcontainergreen = tk.Frame(self.page_elements["greenteam_frame"]["el"], bg="green", height=16)
        lcontainerred = tk.Frame(self.page_elements["redteam_frame"]["el"], bg="red", height=16)
        listcongreen = tk.Frame(self.page_elements["greenteam_frame"]["el"], bg="darkgreen", width=30)
        listconred = tk.Frame(self.page_elements["redteam_frame"]["el"], bg="darkred", width=30, )

        self.green_frame = {
            "green_label_container": {"el": tk.Frame(self.page_elements["greenteam_frame"]["el"], bg="lightgreen"), "opt": {"fill": "x", "side": "top", "expand": False}},
            "green_list_container": {"el": tk.Frame(self.page_elements["greenteam_frame"]["el"], bg="lightgreen"), "opt": {"fill": "both", "side": "bottom", "expand": True}},
            "green_label": {"el": tk.Label(lcontainergreen, text="Green Team", bg="green", font=("Helvetica", 16)), "opt": {"fill": "x", "side": "top"}},
            "green_list": {"el": tk.Listbox(listcongreen, bg="green", width=50, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "left"}},
            "green_list2": {"el": tk.Listbox(listcongreen, bg="darkgreen", width=2, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "right"}}
        }
        self.red_frame = {
            "red_label_container": {"el": tk.Frame(self.page_elements["redteam_frame"]["el"], bg="lightcoral"), "opt": {"fill": "x", "side": "top", "expand": False}},
            "red_list_container": {"el": tk.Frame(self.page_elements["redteam_frame"]["el"], bg="lightcoral"), "opt": {"fill": "both", "side": "bottom", "expand": True}},
            "red_label": {"el": tk.Label(lcontainerred, text="Red Team", bg="red", font=("Helvetica", 16)), "opt": {"fill": "x", "side": "top"}},
            "red_list": {"el": tk.Listbox(listconred, bg="red", width=50, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "right"}},
            "red_list2": {"el": tk.Listbox(listconred, bg="darkred", width=2, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "left"}}
        }
        self.b_con = {

            "b_label_green": {"el": tk.Listbox(self.page_elements["stylized_b_green"]["el"], bg="black", width = 1, font=("Helvetica", 16),fg="white"), "opt": {"fill": "both", "side": "right"}},
            "b_label_red": {"el": tk.Listbox(self.page_elements["stylized_b_red"]["el"], bg="black", width = 1, font=("Helvetica", 16),fg="white"), "opt": {"fill": "both", "side": "right"}}

        }
        # Red Team Containers
        lcontainerred.pack(**self.red_frame["red_label_container"]["opt"])
        self.red_frame["red_label"]["el"].pack(**self.red_frame["red_label"]["opt"])
        listconred.pack(**self.red_frame["red_list_container"]["opt"])
        self.red_frame["red_list"]["el"].pack(**self.red_frame["red_list"]["opt"])
        self.red_frame["red_list2"]["el"].pack(**self.red_frame["red_list"]["opt"])

        # Green Team Containers
        lcontainergreen.pack(**self.green_frame["green_label_container"]["opt"])
        self.green_frame["green_label"]["el"].pack(**self.green_frame["green_label"]["opt"])
        listcongreen.pack(**self.green_frame["green_list_container"]["opt"])
        self.green_frame["green_list"]["el"].pack(**self.green_frame["green_list"]["opt"])
        self.green_frame["green_list2"]["el"].pack(**self.green_frame["green_list"]["opt"])

        self.b_con["b_label_green"]["el"].pack(**self.b_con["b_label_green"]["opt"])
        self.b_con["b_label_red"]["el"].pack(**self.b_con["b_label_red"]["opt"])

        # Add the timer label
 # Place the timer in the middle-top of the screen

        # Start the timer
    def start_timer(self):
        if self.parent.currentwindow == "actionframe":
            self.timer_label = tk.Label(self.window, text="06:00", font=("Helvetica", 48), bg="black", fg="white")
            self.timer_label.place(relx=0.5, rely=0.1, anchor="center") 
            self.remaining_time = 6 * 60  # 6 minutes in seconds
            self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            self.remaining_time -= 1
            if self.parent.currentwindow == "actionframe":
                self.window.after(1000, self.update_timer)

        else:
            # Display "GAME OVER" text in the middle of the screen and make it blink
            self.timer_label.config(text="GAME OVER", font=("Helvetica", 64), fg="red")
            self.timer_label.place(relx=0.5, rely=0.5, anchor="center")  # Center the "GAME OVER" text
            self.blink_game_over()

    def blink_game_over(self):
        current_color = self.timer_label.cget("fg")
        new_color = "black" if current_color == "red" else "red"
        self.timer_label.config(fg=new_color)
        self.window.after(500, self.blink_game_over)  # Toggle color every 500ms

    def setbuttonfunction(self, functosend):
        self.buttonfunc = lambda: functosend

    def append_user(self, team: bool, name: str, score):
        if team:
            print("appending red user")
            self.red_frame["red_list"]["el"].insert(tk.END, f"{name.rjust(20)}")
            self.red_frame["red_list2"]["el"].insert(tk.END, f"{score}")
        else:
            print("user append green user")
            self.green_frame["green_list"]["el"].insert(tk.END, f"{name.rjust(20)}")
            self.green_frame["green_list2"]["el"].insert(tk.END, f"{score}")
            #self.b_con["b_label_green"]["el"].insert(tk.END, "B")

    def append_list(self, listofusers: dict):
        print("appendint_list")
        for key, player in listofusers.items():
            if player.team == "RED TEAM":

                print(f"r {player}")
                self.append_user(True, player.name, player.score)

            elif player.team == "GREEN TEAM":
                print(f"g {player}")
                self.append_user(False, player.name, player.score)
            else:
                print(f"e {player}")
                self.append_user(random.choice([True, False]), player.name, player.score)

        # loop though red team and apend users
        # loop through green team and apend users



    # def stylized_b(self, listofusers: list):

    #     for player in listofusers:
    #         if player.base_score == 3:
    #             index = listofusers.index(player)
    #             self.b_con["b_label_green"]["el"].insert(index, "B")

    def stylized_b(self, listofusers: list, name: str, base_score: int):
        #loop through all the players
        for player in listofusers:
            #add empty items to Listbox
            self.b_con["b_label_green"]["el"].insert(tk.END, "")
            self.b_con["b_label_red"]["el"].insert(tk.END, "")
            #check for what team a player is on
            if player[3] == "GREEN TEAM" and player[2] == name:
                #check the score passed through from the server
                if base_score == 3:
                    self.b_con["b_label_green"]["el"].insert(listofusers.index(player), "B")

            if player[3] == "RED TEAM" and player[2] == name:
                if base_score == 3:
                    self.b_con["b_label_red"]["el"].insert(listofusers.index(player), "B")




class actionFrame2(page):  # example of how a page could be implemented
    def __init__(self, parent: window):
        super().__init__()
        self.parent = parent
        self.page_elements = {
            "redteam_frame": {"el": tk.Frame(self.window, bg="blue", width="100"), "opt": {"fill": "both", "side": "right", "expand": True}},
            "greenteam_frame": {"el": tk.Frame(self.window, bg="red", width="100"), "opt": {"fill": "both", "side": "left", "expand": True}},
            "split_frame": {"el": tk.Frame(self.window, bg="black"), "opt": {"fill": "both", "side": "left", "expand": True}},
        }
        self.middle = {"button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="back", command=lambda: self.parent.switch_window("actionscreen")), "opt": {}}}
        self.middle_frame = {}
        self.redFrame = {}
        self.middle["button"]["el"].pack()

def change_network_popup():
    popup = tk.Toplevel()
    popup.title("Popup Window")
    popup.geometry("300x150")
    tk.Label(popup, text="Changing network to IP", font=("Helvetica", 14)).pack(pady=20)
    entry = tk.Entry(popup, font=("Helvetica", 12))
    entry.pack(pady=5)

    def submit():
        new_ip = entry.get()
        print(f"Changing network to IP: {new_ip}")
        print(f"AHHHH: {new_ip}")
        game_handler.change_socket(new_ip)
        popup.destroy()
    tk.Button(popup, text="Submit", command=submit).pack(pady=10)
def start_game_with_countdown(parent: window, list_of_id_and_names,event=None,):
    global teams
    teams = list_of_id_and_names

    from countdown_timer import CountdownTimer
    CountdownTimer(parent, lambda: countdown_to_playaction(parent))


def countdown_to_playaction(parent: window):
    # self.app.destroy()
    print("Countdown finished, switching to ActionFrame screen...")
    # New window initialized
    parent.switch_window("actionframe")
    print(parent.pages)
    parent.pages['actionframe'].start_timer()


class splashFrame(page):
    def __init__(self, parent: window):
        super().__init__(parent)
        print("SplashFrame initializing...")

        self.parent.window.bind("<Escape>", lambda e: self.parent.window.destroy())
        window_width = self.parent.window.winfo_screenwidth()
        window_height = self.parent.window.winfo_screenheight()

        # Load and resize image
        image_path = os.path.join(os.path.dirname(__file__), "assets/images/logo.jpg")
        image = Image.open(image_path)
        resized_image = image.resize((window_width, window_height))
        self.tk_image = ImageTk.PhotoImage(resized_image)  # Keep reference

        splash_label = tk.Label(self.parent.window, image=self.tk_image)
        self.page_elements = {
            "splash_frame": {
                "el": splash_label,
                "opt": {"fill": "both", "expand": True}
            }
        }

        def next_screen():
            self.parent.switch_window("playerframe")
        self.parent.window.after(3000, next_screen)

class playerFrame(page):
    def __init__(self,parent: window):
        super().__init__(parent)
        self.window = parent.window
        self.parent = parent
        self.teams = []
        self.green_entries = []
        self.red_entries = []
        self.change_network = lambda: change_network_popup()
        self.parent.window.bind("<F5>", lambda e: start_game_with_countdown(self.parent,self.teams))
        self.parent.window.bind("<Return>", lambda e: get_entry_value(self))
        self.parent.window.bind("<F12>", lambda e: delete_entries(self))
        self.get_entries_button = lambda: get_entry_value(self)
        self.clear_entries_button = lambda: delete_entries(self)
        self.start_button = lambda: start_game_with_countdown(self.parent, self.teams)
        # set function that button will call here or set it with the function setbuttonfunction(func)
        def get_entry_value(self):
            # get entry value for green team
            for id_entry,eqid_entry, name_entry in self.green_entries:
                new_id = id_entry.get()
                new_eqid = eqid_entry.get()
                new_name = name_entry.get()
                if new_id or new_name or new_eqid:  # Ignore empty entries
                    self.teams.append((new_id, new_eqid, new_name, "GREEN TEAM" ))
                    game_handler.add_player(new_name, new_id, new_eqid, "GREEN TEAM")
                    print("adding GREEN team guy")

            # get entry value for red team
            for id_entry,eqid_entry, name_entry in self.red_entries:
                new_id = id_entry.get()
                new_eqid = eqid_entry.get()
                new_name = name_entry.get()
                if new_id or new_name or new_eqid:  # Ignore empty entries
                    self.teams.append((new_id, new_eqid, new_name, "RED TEAM"))
                    game_handler.add_player(new_name, new_id, new_eqid, "RED TEAM")
                    print("adding RED team guy")
            print(f"test {game_handler.get_list_of_usrs()}")
            parent.pages['actionframe'].append_list(game_handler.get_list_of_usrs())

        def delete_entries(self):
            # delete entries value for green team
            for id_entry,eqid_entry, name_entry in self.green_entries:
                new_id = id_entry.delete(0, tk.END)
                new_eqid = eqid_entry.delete(0, tk.END)
                new_name = name_entry.delete(0, tk.END)
            # delete entries value for red team
            for id_entry,eqid_entry, name_entry in self.red_entries:
                new_id = id_entry.delete(0, tk.END)
                new_eqid = eqid_entry.delete(0, tk.END)
                new_name = name_entry.delete(0, tk.END)

        self.page_elements = {
            "redteam_frame": {"el": tk.Frame(self.window, bg="red", width=200), "opt": {"fill": "both", "side": "right", "expand": False}},
            "greenteam_frame": {"el": tk.Frame(self.window, bg="green", width=200), "opt": {"fill": "both", "side": "left", "expand": False}},
            "split_frame": {"el": tk.Frame(self.window, bg="black"), "opt": {"fill": "both", "side": "left", "expand": True}},
        }
        self.middle = {

            "start_button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="start game <F5>", command=self.start_button), "opt": {}},
            "get_entries_button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="get entries <Enter>", command=self.get_entries_button), "opt": {}},
            "clear_entries_button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="clear entries <F12>", command=self.clear_entries_button), "opt": {}},
            "change_network_button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="Change Network", command=self.change_network), "opt": {"anchor": "center"}}}
        # stupid dumb fix because we didn't use html and typescript

        lcontainergreen = tk.Frame(self.page_elements["greenteam_frame"]["el"], bg="green", height=16)
        lcontainerred = tk.Frame(self.page_elements["redteam_frame"]["el"], bg="red", height=16)
        listcongreen = tk.Frame(self.page_elements["greenteam_frame"]["el"], bg="darkgreen", width=30)
        listconred = tk.Frame(self.page_elements["redteam_frame"]["el"], bg="darkred", width=30, )

         # --- GREEN LABEL ROW FRAME ---
        green_label_row = tk.Frame(listcongreen, bg="green")
        green_label_row.pack(fill="x", side="top")

        # --- RED LABEL ROW FRAME ---
        red_label_row = tk.Frame(listconred, bg="red")
        red_label_row.pack(fill="x", side="top")


        # GREEN ENTRY ROWS
        for i in range(15):
            row = tk.Frame(listcongreen, bg="lightgreen")
            row.pack(fill="x", pady=2)

            tk.Label(row, text=f"{i+1}", bg="lightgreen", width=5).pack(side="left")

            player_id = tk.Entry(row, width=20)
            player_id.pack(side="left", padx=10)

            equip_id = tk.Entry(row, width=20)
            equip_id.pack(side="left", padx=10)

            player_name = tk.Entry(row, width=20)
            player_name.pack(side="left", padx=10)

            self.green_entries.append((player_id, equip_id, player_name))


        # RED ENTRY ROWS
        for i in range(15):
            row = tk.Frame(listconred, bg="red")
            row.pack(fill="x", pady=2)

            tk.Label(row, text=f"{i+1}", bg="red", width=5).pack(side="left", padx=5)

            player_id = tk.Entry(row, width=20)
            player_id.pack(side="left", padx=10)

            equip_id = tk.Entry(row, width=20)
            equip_id.pack(side="left", padx=10)

            player_name = tk.Entry(row, width=20)
            player_name.pack(side="left", padx=10)

            self.red_entries.append((player_id, equip_id, player_name))

        self.green_frame = {
            "green_label_container": {"el": tk.Frame(self.page_elements["greenteam_frame"]["el"], bg="lightgreen"), "opt": {"fill": "x", "side": "top", "expand": False}},
            "green_list_container": {"el": tk.Frame(self.page_elements["greenteam_frame"]["el"], bg="lightgreen"), "opt": {"fill": "both", "side": "bottom", "expand": True}},
            "green_label": {"el": tk.Label(lcontainergreen, text="Green Team", bg="green", font=("Helvetica", 16)), "opt": {"fill": "x", "side": "top"}},
            "green_list": {"el": tk.Listbox(listcongreen, bg="green", width=50, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "left"}},
            "green_label_1": {"el": tk.Label(green_label_row, text="Player ID", bg="lightgreen", font=("Helvetica", 12)), "opt": {"side": "left", "expand": True, "padx": 5}},
            "green_label_2" : {"el": tk.Label(green_label_row, text="Equipment ID", bg="lightgreen", font=("Helvetica", 12)), "opt": {"side": "left", "expand": True, "padx": 5}},
            "green_label_3" : {"el": tk.Label(green_label_row, text="Player Name", bg="lightgreen", font=("Helvetica", 12)), "opt": {"side": "left", "expand": True, "padx": 5}}
        }
        self.red_frame = {
            "red_label_container": {"el": tk.Frame(self.page_elements["redteam_frame"]["el"], bg="lightcoral"), "opt": {"fill": "x", "side": "top", "expand": False}},
            "red_list_container": {"el": tk.Frame(self.page_elements["redteam_frame"]["el"], bg="lightcoral"), "opt": {"fill": "both", "side": "bottom", "expand": True}},
            "red_label": {"el": tk.Label(lcontainerred, text="Red Team", bg="red", font=("Helvetica", 16)), "opt": {"fill": "x", "side": "top"}},
            "red_list": {"el": tk.Listbox(listconred, bg="red", width=50, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "right"}},
            "red_label_1" : {"el": tk.Label(red_label_row, text="Player ID", bg="lightcoral", font=("Helvetica", 12)), "opt": {"side": "left", "expand": True, "padx": 5}},
            "red_label_2" : {"el": tk.Label(red_label_row, text="Equipment ID", bg="lightcoral", font=("Helvetica", 12)), "opt": {"side": "left", "expand": True, "padx": 5}},
            "red_label_3" : {"el": tk.Label(red_label_row, text="Player Name", bg="lightcoral", font=("Helvetica", 12)), "opt": {"side": "left", "expand": True, "padx": 5}}
        }

        self.middle["change_network_button"]["el"].pack(**self.middle["change_network_button"]["opt"])
        self.middle["get_entries_button"]["el"].pack(**self.middle["get_entries_button"]["opt"])
        self.middle["clear_entries_button"]["el"].pack(**self.middle["clear_entries_button"]["opt"])
        self.middle["start_button"]["el"].pack(**self.middle["start_button"]["opt"])

        # Red Team Containers
        lcontainerred.pack(**self.red_frame["red_label_container"]["opt"])
        self.red_frame["red_label"]["el"].pack(**self.red_frame["red_label"]["opt"])
        listconred.pack(**self.red_frame["red_list_container"]["opt"])
        self.red_frame["red_list"]["el"].pack(**self.red_frame["red_list"]["opt"])
        red_label_row.pack(fill="x", side="top")

        # Red labels (horizontal)
        self.red_frame["red_label_1"]["el"].pack(**self.red_frame["red_label_1"]["opt"])
        self.red_frame["red_label_2"]["el"].pack(**self.red_frame["red_label_2"]["opt"])
        self.red_frame["red_label_3"]["el"].pack(**self.red_frame["red_label_3"]["opt"])

        # Green Team Containers
        lcontainergreen.pack(**self.green_frame["green_label_container"]["opt"])
        self.green_frame["green_label"]["el"].pack(**self.green_frame["green_label"]["opt"])
        listcongreen.pack(**self.green_frame["green_list_container"]["opt"])
        self.green_frame["green_list"]["el"].pack(**self.green_frame["green_list"]["opt"])
        green_label_row.pack(fill="x", side="top")

        # Green labels (horizontal)
        self.green_frame["green_label_1"]["el"].pack(**self.green_frame["green_label_1"]["opt"])
        self.green_frame["green_label_2"]["el"].pack(**self.green_frame["green_label_2"]["opt"])
        self.green_frame["green_label_3"]["el"].pack(**self.green_frame["green_label_3"]["opt"])
