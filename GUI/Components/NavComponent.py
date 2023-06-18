# Imports needed
import tkinter as tk
from PIL import Image, ImageTk


class NavComponent(tk.Frame):
    """This class is used to create the navigation bar that will be used in the main window."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0F0F0", pady=10)

        self.controller = controller

        # Create the images for the buttons
        manage_img = Image.open("GUI/res/manage.png").resize((20, 20))
        settings_img = Image.open("GUI/res/settings.png").resize((20, 20))
        logs_img = Image.open("GUI/res/logs.png").resize((20, 20))
        home_img = Image.open("GUI/res/home.png").resize((20, 20))

        self.manage_photo = ImageTk.PhotoImage(manage_img)
        self.settings_photo = ImageTk.PhotoImage(settings_img)
        self.logs_photo = ImageTk.PhotoImage(logs_img)
        self.home_photo = ImageTk.PhotoImage(home_img)

        button_width = 10
        button_font = ("Arial", 12)

        # TODO: Find a better coloring scheme for the buttons (Adobe Color?)

        self.home_btn = tk.Button(self, text="Home", image=self.home_photo, compound="left", padx=10, pady=5,
                                  font=button_font, bd=0,
                                  command=lambda: controller.change_view("HomeView"), width=button_width)

        self.manage_btn = tk.Button(self, text="Manage", image=self.manage_photo, compound="left", padx=10, pady=5,
                                    font=button_font, bd=0, command=lambda: self.controller.change_view("ManageView"),
                                    width=button_width)
        self.settings_btn = tk.Button(self, text="Settings", image=self.settings_photo, compound="left", padx=10,
                                      pady=5,
                                      font=button_font, bd=0, command=lambda: controller.change_view("SettingsView"),
                                      width=button_width)
        self.logs_btn = tk.Button(self, text="Logs", image=self.logs_photo, compound="left", padx=10, pady=5,
                                  font=button_font, bd=0, command=lambda: controller.change_view("LogsView"),
                                  width=button_width)

        # TODO: Dynamically changing size not working?

        self.home_btn.pack(side="left", padx=10, fill="both", expand=True)
        self.manage_btn.pack(side="left", padx=10, fill="both", expand=True)
        self.settings_btn.pack(side="left", padx=10, fill="both", expand=True)
        self.logs_btn.pack(side="left", padx=10, fill="both", expand=True)

    def active_btn(self):

        # Variables for the colors
        golden_color = "#FFD700"
        n_button_bg = "#D3D3D3"
        button_active_bg = "#A9A9A9"
        button_fg = "#000000"

        # Set all the colors to the default
        self.home_btn.configure(bg=n_button_bg, activebackground=button_active_bg, fg=button_fg)
        self.manage_btn.configure(bg=n_button_bg, activebackground=button_active_bg, fg=button_fg)
        self.settings_btn.configure(bg=n_button_bg, activebackground=button_active_bg, fg=button_fg)
        self.logs_btn.configure(bg=n_button_bg, activebackground=button_active_bg, fg=button_fg)

        # Current page will have its corresponding button highlighted in Gold
        if self.controller.current_page == "HomeView":
            self.home_btn.configure(bg=golden_color, activebackground=golden_color)
        elif self.controller.current_page == "ManageView":
            self.manage_btn.configure(bg=golden_color, activebackground=golden_color)
        elif self.controller.current_page == "SettingsView":
            self.settings_btn.configure(bg=golden_color, activebackground=golden_color)
        elif self.controller.current_page == "LogsView":
            self.logs_btn.configure(bg=golden_color, activebackground=golden_color)
