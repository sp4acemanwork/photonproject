import tkinter as tk
import random
from server import handler
from PIL import  Image, ImageTk
game_handler = handler("127.0.0.1", 7502, 1024)
import os

# import keyboard # implement later

class page:
    def __init__(self, parent_window: tk.Tk):
        self.window = parent_window
        self.page_elements = {}
        self.setvis = True
        


class window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.attributes("-zoomed", True)
        self.currentwindow = None
        self.pages = {}
        

    def addPage(self, name: str, el: page):
        self.pages[name] = el

    def redraw(self, windowname: str):
        print("packpages")

        page = self.pages[windowname]
        self.currentwindow = windowname
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
        self.hidepage()
        self.redraw(windowname)


class actionFrame(page):  # example of how a page could be implemented
    def __init__(self, parent_window: tk.Tk, parent: window):  # could horribly backfire
        super().__init__(parent_window)
        self.parent_window = parent_window
        self.parent = parent
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
            "green_list": {"el": tk.Listbox(listcongreen, bg="green", width=20, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "left"}},
            "green_list2": {"el": tk.Listbox(listcongreen, bg="darkgreen", width=2, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "right"}}
        }
        self.red_frame = {
            "red_label_container": {"el": tk.Frame(self.page_elements["redteam_frame"]["el"], bg="lightcoral"), "opt": {"fill": "x", "side": "top", "expand": False}},
            "red_list_container": {"el": tk.Frame(self.page_elements["redteam_frame"]["el"], bg="lightcoral"), "opt": {"fill": "both", "side": "bottom", "expand": True}},
            "red_label": {"el": tk.Label(lcontainerred, text="Red Team", bg="red", font=("Helvetica", 16)), "opt": {"fill": "x", "side": "top"}},
            "red_list": {"el": tk.Listbox(listconred, bg="red", width=20, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "right"}},
            "red_list2": {"el": tk.Listbox(listconred, bg="darkred", width=2, font=("Helvetica", 16)), "opt": {"fill": "both", "side": "left"}}
        }
        self.b_con = {

            "b_label_green": {"el": tk.Listbox(self.page_elements["stylized_b_green"]["el"], bg="black", width = 1, font=("Helvetica", 16),fg="white"), "opt": {"fill": "both", "side": "right"}},
            "b_label_red": {"el": tk.Listbox(self.page_elements["stylized_b_red"]["el"], bg="black", width = 1, font=("Helvetica", 16),fg="white"), "opt": {"fill": "both", "side": "right"}}

        }
        self.middle["button"]["el"].pack()
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

    def setbuttonfunction(self, functosend):
        self.buttonfunc = lambda: functosend

    def append_user(self, team: bool, name: str, id: str):
        score: int = 0
        if team:
            print("appending red user")
            self.red_frame["red_list"]["el"].insert(tk.END, f"{name.rjust(20)}")
            self.red_frame["red_list2"]["el"].insert(tk.END, f"{score}")
            
        else:
            print("user append green user")
            self.green_frame["green_list"]["el"].insert(tk.END, f"{name.rjust(20)}")
            self.green_frame["green_list2"]["el"].insert(tk.END, f"{score}")
            #self.b_con["b_label_green"]["el"].insert(tk.END, "B")

    def append_list(self, listofusers: list):
        print("appendint_list")
        for player in listofusers:
            if player[3] == "RED TEAM":

                print(f"r {player}")
                self.append_user(True, player[2], player[1])

            elif player[3] == "GREEN TEAM":
                print(f"g {player}")
                self.append_user(False, player[2], player[1])
            else:
                print(f"e {player}")
                self.append_user(random.choice([True, False]), player[2], player[1])

        # loop though red team and apend users
        # loop through green team and apend users

        


    # def stylized_b(self, listofusers: list):

    #     for player in listofusers:
    #         if player.base_score == 3:
    #             index = listofusers.index(player)
    #             self.b_con["b_label_green"]["el"].insert(index, "B")

    def stylized_b(self, listofusers: list):
        
        #loop through all the players
        for player in listofusers:
            #add empty items to Listbox
            self.b_con["b_label_green"]["el"].insert(tk.END, "")
            self.b_con["b_label_red"]["el"].insert(tk.END, "")
            #check for what team a player is on
            if player[3] == "GREEN TEAM":
                #check the score passed through from the server
                if player.base_score == 3:
                    self.b_con["b_label_green"]["el"].insert(listofusers.index(player), "B")

            if player[3] == "RED TEAM":
                
                if player.base_score == 3:
                    self.b_con["b_label_red"]["el"].insert(listofusers.index(player), "B")
                
        




class actionFrame2(page):  # example of how a page could be implemented
    def __init__(self, parent_window: window, parent: window):
        super().__init__(parent_window)
        self.parent_window = parent_window
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
def start_game_with_countdown(parent, list_of_id_and_names,event=None,):
    global teams
    teams = list_of_id_and_names

    from countdown_timer import CountdownTimer  
    CountdownTimer(parent, lambda: countdown_to_playaction(parent))

def countdown_to_playaction(parent):
    # self.app.destroy()
    parent.destroy()
    print("Countdown finished, switching to ActionFrame screen...")
    # New window initialized
    test = window()
    testpage = actionFrame(test.window, test)
    test.addPage("actionscreen", testpage)
    test.redraw("actionscreen")
    testpage.append_list(teams)

class splashFrame(page):
    def __init__(self, parent_window: window, parent: window):
        super().__init__(parent_window)
        self.parent_window = parent_window
        self.parent = parent
        self.parent.window.bind("<Escape>", lambda e: self.parent.window.destroy())
        window_width = self.parent.window.winfo_screenwidth()
        window_height = self.parent.window.winfo_screenheight()

        # Used os module to get the path of the image dynamically
        image_path = os.path.join(os.path.dirname(__file__), "assets/images/logo.jpg")
        image = Image.open(image_path)
        resized_image = image.resize((window_width, window_height))
        tk_image = ImageTk.PhotoImage(resized_image)

        self.page_elements = {
            "splash_frame": {"el": tk.Label(self.parent.window, image=tk_image, text=""), "opt": {"expand":True}},
        }
        self.page_elements["splash_frame"]["el"].pack(**self.page_elements["splash_frame"]["opt"])
        

        def next_screen():
            self.parent.window.destroy()
            test = window()
            testpage = playerFrame(test.window, test)
            test.addPage("playerscreen", testpage)

            test.redraw("playerscreen")
            test.window.mainloop()

        self.parent.window.after(3000, next_screen)
        self.parent.window.mainloop()

class playerFrame(page):
    def __init__(self, parent_window: window, parent: window):
        super().__init__(parent_window)
        self.parent_window = parent_window
        self.parent = parent
        self.teams = []
        self.green_entries = []
        self.red_entries = []
        self.change_network = lambda: change_network_popup()
        self.parent.window.bind("<F5>", lambda e: start_game_with_countdown(self.parent.window,self.teams))
        self.parent.window.bind("<Return>", lambda e: get_entry_value(self))
        self.parent.window.bind("<F12>", lambda e: delete_entries(self))
        self.buttonfunc = lambda: self.parent.switch_window("test")  # set function that button will call here or set it with the function setbuttonfunction(func)
        
        def get_entry_value(self):
            # get entry value for green team
            for id_entry,eqid_entry, name_entry in self.green_entries:
                new_id = id_entry.get()
                new_eqid = eqid_entry.get()
                new_name = name_entry.get()
                if new_id or new_name or new_eqid:  # Ignore empty entries
                    self.teams.append((new_id, new_eqid, new_name, "GREEN TEAM" ))
                    game_handler.add_player(new_name, new_id, new_eqid)

            # get entry value for red team
            for id_entry,eqid_entry, name_entry in self.red_entries:
                new_id = id_entry.get()
                new_eqid = eqid_entry.get()
                new_name = name_entry.get()
                if new_id or new_name or new_eqid:  # Ignore empty entries
                    self.teams.append((new_id, new_eqid, new_name, "RED TEAM" ))
                    game_handler.add_player(new_name, new_id, new_eqid)

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
        self.middle = {"back_button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="back", command=self.buttonfunc), "opt": {}},
                       "change_network_button": {"el" : tk.Button(self.page_elements["split_frame"]["el"], text="Change Network", command=self.change_network), "opt": {"anchor" :"center"}}}
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
       

        self.middle["back_button"]["el"].pack()
        self.middle["change_network_button"]["el"].pack(**self.middle["change_network_button"]["opt"])
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







<<<<<<< HEAD
# test = window()
# testpage = actionFrame(test.window, test)
# testpage2 = actionFrame2(test.window, test)
# test.addPage("actionscreen", testpage)
# example_list = [
#     (1, 101, "Alice", "RED TEAM"),
#     (2, 102, "Bob", "GREEN TEAM"),
#     (3, 103, "Charlie", "RED TEAM"),
#     (4, 104, "David", "GREEN TEAM"),
#     (5, 105, "Eve", "RED TEAM"),
#     (6, 106, "Frank", "GREEN TEAM"),
#     (7, 107, "Grace", "RED TEAM"),
#     (8, 108, "Hank", "GREEN TEAM")
# ]
=======

test = window()
testpage = actionFrame(test.window, test)
testpage2 = actionFrame2(test.window, test)
test.addPage("actionscreen", testpage)
example_list = [
    (1, 101, "Alice", "RED TEAM"),
    (2, 102, "Bob", "GREEN TEAM"),
    (3, 103, "Charlie", "RED TEAM"),
    (4, 104, "David", "GREEN TEAM"),
    (5, 105, "Eve", "RED TEAM"),
    (6, 106, "Frank", "GREEN TEAM"),
    (7, 107, "Grace", "RED TEAM"),
    (8, 108, "Hank", "GREEN TEAM")
]
>>>>>>> 63aa40d (working on the stylized b, almost done)

testpage.append_list(example_list)
testpage.stylized_b(example_list)
test.addPage("test", testpage2)
test.redraw("actionscreen")
test.window.mainloop()

# TEST
# test = window()
# testpage = playerFrame(test.window, test)
# test.addPage("playerscreen", testpage)

# test.redraw("playerscreen")
# test.window.mainloop()

# '''
# window = tk.Tk()
# testlabel = tk.Label(window, text='test')
# testlabel.pack()
# window.mainloop()
# '''
