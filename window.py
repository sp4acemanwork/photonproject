from tkinter import Label
from tkinter import Button
import tkinter as tk

# import keyboard # implement later


class window:
    def __init__(self):
        self.window = tk.Tk()
        test2 = tk.Button(self.window, text="this button works", width=10, command=self.window.destroy)
        testlabel = tk.Label(self.window, text='test')
        testlabel.pack()
        test2.pack()
        self.window_elements = {
            "test": tk.Button(self.window, text="test", width=10, command=self.window.destroy),
            "test1": tk.Button(self.window, text="test", width=10, command=self.window.destroy),
            "test2": tk.Button(self.window, text="test", width=10, command=self.window.destroy),
            "test3": tk.Button(self.window, text="test", width=10, command=self.window.destroy)

        }

    def redraw(self):
        for key in self.window_elements:
            test = self.window_elements[key]
            test.pack()


test = window()
test.redraw()
test.window.mainloop()
'''
window = tk.Tk()
testlabel = tk.Label(window, text='test')
testlabel.pack()
window.mainloop()
'''
