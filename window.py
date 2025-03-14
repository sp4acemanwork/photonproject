from tkinter import Label
from tkinter import Button
import tkinter as tk

# import keyboard # implement later


class page:
    def __init__(self, parrent_window: tk.Tk):
        self.window = parrent_window
        self.page_elements = {}
        self.setvis = True


class actionFrame(page): # example of how a page could be implemented
    def __init__(self, parrent_window: tk.Tk):
        super().__init__(parrent_window)
        self.page_elements = {
            "redteam_frame": {"el": tk.Frame(self.window, bg="red", width="100p"), "opt": {"fill": "both", "side": "right", "expand": True}},
            "greenteam_frame": {"el": tk.Frame(self.window, bg="green", width="100p"), "opt": {"fill": "both", "side": "left", "expand": True}},
            "split_frame": {"el": tk.Frame(self.window, bg="black"), "opt": {"fill": "both", "side": "left", "expand": True}},
        }


class window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.pages = {}

    def addPage(self, name: str, el: page):
        self.pages[name] = el

    def redraw(self):
        print("packpages")
        for key in self.pages:  # Loop over self.pages, not the class
            page = self.pages[key]
            for element in page.page_elements.values():  # Access the page elements
                element["el"].pack(**element["opt"])  # Pack each element
                print(f"packing{0} ", element)


test = window()
testpage = actionFrame(test.window)
test.addPage("actionscreen", testpage)
test.redraw()
test.window.mainloop()

'''
window = tk.Tk()
testlabel = tk.Label(window, text='test')
testlabel.pack()
window.mainloop()
'''
