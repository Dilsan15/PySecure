import tkinter as tk


class SettingsView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # TODO: Get rid of boilerplate test code and figure out which user settings we want and how we will save
        #  them, (what is AppData?)

        self.controller = controller
        page_title = tk.Label(self, text="Settings")
        page_title.pack(side='top', fill="x", pady=10)
