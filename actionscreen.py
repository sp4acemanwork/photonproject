from window import window
import tkinter as tk


class action_actionscreen(window):
    def __init__(self):
        # self.window exists
        # this is a dumb fix
        super().__init__()
        self.window.geometry("800x900")
        self.redteam_frame = {}
        self.greenteam_frame = {}
        self.window_elements = {
            "redteam_frame": tk.Frame(self.window, bg="red"),
            "greenteam_frame": tk.Frame(self.window, bg="green" )

        }

    def draw(self):
        self.window_elements["redteam_frame"].pack(fill='both', side='left', expand='True')
        self.window_elements["greenteam_frame"].pack(fill='both', side='left', expand='True')

        self.window_elements["redteam_frame"].pack_propagate(0)
        self.window_elements["greenteam_frame"].pack_propagate(0)
        # why must we call pack(location) to determine the location of objects


acctest = action_actionscreen()

acctest.draw()
acctest.window.mainloop()



