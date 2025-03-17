import tkinter as tk
import random
# import keyboard # implement later


class page:
    def __init__(self, parrent_window: tk.Tk):
        self.window = parrent_window
        self.page_elements = {}
        self.setvis = True


class window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
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
    def __init__(self, parrent_window: tk.Tk, parrent: window):  # could horribly backfire
        super().__init__(parrent_window)
        self.parrent_window = parrent_window
        self.parrent = parrent
        self.buttonfunc = lambda: self.parrent.switch_window("test")  # set function that button will call here or set it with the function setbuttonfunction(func)
        self.page_elements = {
            "redteam_frame": {"el": tk.Frame(self.window, bg="red", width=60), "opt": {"fill": "both", "side": "right", "expand": False}},
            "greenteam_frame": {"el": tk.Frame(self.window, bg="green", width=60), "opt": {"fill": "both", "side": "left", "expand": False}},
            "split_frame": {"el": tk.Frame(self.window, bg="black"), "opt": {"fill": "both", "side": "left", "expand": True}},
        }
        self.middle = {"button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="back", command= self.buttonfunc), "opt": {}}}
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

    def setbuttonfunction(self, functosent):
        self.buttonfunc = lambda: functosent

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
        # loop through green team and apand users


class actionFrame2(page):  # example of how a page could be implemented
    def __init__(self, parrent_window: window, parrent: window):
        super().__init__(parrent_window)
        self.parrent_window = parrent_window
        self.parrent = parrent
        self.page_elements = {
            "redteam_frame": {"el": tk.Frame(self.window, bg="blue", width="100p"), "opt": {"fill": "both", "side": "right", "expand": True}},
            "greenteam_frame": {"el": tk.Frame(self.window, bg="red", width="100p"), "opt": {"fill": "both", "side": "left", "expand": True}},
            "split_frame": {"el": tk.Frame(self.window, bg="black"), "opt": {"fill": "both", "side": "left", "expand": True}},
        }
        self.middle = {"button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="back", command=lambda: self.parrent.switch_window("actionscreen")), "opt": {}}}
        self.middle_frame = {}
        self.redFrame = {}
        self.middle["button"]["el"].pack()


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

testpage.append_list(example_list)
test.addPage("test", testpage2)
test.redraw("actionscreen")
test.window.mainloop()

'''
window = tk.Tk()
testlabel = tk.Label(window, text='test')
testlabel.pack()
window.mainloop()
'''
