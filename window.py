from tkinter import Label
from tkinter import Button
import tkinter as tk

# import keyboard # implement later



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
        key = self.currentwindow
        page = self.pages[key]
        for element in page.page_elements.values():  # Access the page elements
            element["el"].pack_forget()  # Pack each element
            print(f"unpacking{0} ", element)

    def switch_window(windowname: str):

        print("switchingwindow")


class page:
    def __init__(self, parrent_window: window):
        self.window = parrent_window
        self.page_elements = {}
        self.setvis = True


class actionFrame(page):  # example of how a page could be implemented
    def __init__(self, parrent_window: window):
        super().__init__(parrent_window)
        self.parrent = parrent_window
        self.page_elements = {
            "redteam_frame": {"el": tk.Frame(self.window, bg="red", width="100p"), "opt": {"fill": "both", "side": "right", "expand": True}},
            "greenteam_frame": {"el": tk.Frame(self.window, bg="green", width="100p"), "opt": {"fill": "both", "side": "left", "expand": True}},
            "split_frame": {"el": tk.Frame(self.window, bg="black"), "opt": {"fill": "both", "side": "left", "expand": True}},
        }
        self.middle = {"button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="test", command=parrent_window.switch_window("test")), "opt": {}}}
        self.middle_frame = {}
        self.redFrame = {}
        self.middle["button"]["el"].pack()


class actionFrame2(page):  # example of how a page could be implemented
    def __init__(self, parrent_window: window):
        super().__init__(parrent_window)
        self.parrent = parrent_window
        self.page_elements = {
            "redteam_frame": {"el": tk.Frame(self.window, bg="blue", width="100p"), "opt": {"fill": "both", "side": "right", "expand": True}},
            "greenteam_frame": {"el": tk.Frame(self.window, bg="red", width="100p"), "opt": {"fill": "both", "side": "left", "expand": True}},
            "split_frame": {"el": tk.Frame(self.window, bg="black"), "opt": {"fill": "both", "side": "left", "expand": True}},
        }
        self.middle = {"button": {"el": tk.Button(self.page_elements["split_frame"]["el"], text="test", command=parrent_window.switch_window("actionscreen")), "opt": {}}}
        self.middle_frame = {}
        self.redFrame = {}
        self.middle["button"]["el"].pack()


test = window()
testpage = actionFrame(test.window)
testpage = actionFrame2(test.window)
test.addPage("actionscreen", testpage)

test.addPage("test", testpage)
test.redraw("actionscreen")
test.window.mainloop()

'''
window = tk.Tk()
testlabel = tk.Label(window, text='test')
testlabel.pack()
window.mainloop()
'''
