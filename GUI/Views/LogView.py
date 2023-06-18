import tkinter as tk


class LogsView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # TODO Get rid of the boilerplate test code and start figuring out the logging system (SQL Vs CSV??)
        self.controller = controller

        page_title = tk.Label(self, text="Logs")
        page_title.pack(side='top', fill="x", pady=10)
