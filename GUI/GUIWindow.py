# Import Libraries

import tkinter as tk
import os
import importlib
from .Components import NavComponent
import sys


class GUIWindow(tk.Tk):
    """Main GUI Window, Frames will be build on top of this. Kind of serving a secondary controller, which was unintended"""

    def __init__(self, controller, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.controller = controller

        # Sets basic features of the app
        self.geometry("800x700")
        self.title('PySecure')

        self.iconphoto(True, tk.PhotoImage(file="GUI/res/lock.png"))

        # Hard to make Tk Dynamic so its best to just disable resizing
        self.resizable(False, False)

        # Use of NavComponent
        self.nav_bar = NavComponent(self, self.controller)
        self.nav_bar.pack(side="top", fill='x', pady=10)

        # Setting up the container for the frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.configure(bg='gray')

        # Dictionary of all the frames
        self.frames = {}

        package_path = os.path.join(os.path.dirname(__file__), 'Views')

        # Copilot wrote the initial code for this, it didn't work because of the way the .pyfiles was structured
        # I changed it using importlib and documentation

        # TODO: Make this code more readable and why is it so chunky?

        # Essentially this code is going through the Views folder and placing all the View Classes into a list
        for dir_path, _, filenames in os.walk(package_path):
            for filename in filenames:
                if filename.endswith('View.py'):
                    module_name = os.path.splitext(filename)[0]
                    module_name = "Views." + module_name
                    module_path = os.path.join(dir_path, filename)

                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[module_name] = module
                    spec.loader.exec_module(module)

                    module_classes = [
                        obj
                        for obj in vars(module).values()
                        if isinstance(obj, type)
                    ]

                    for frame in module_classes:
                        print(frame)
                        frame = frame(container, self.controller)
                        frame.grid(row=0, column=0, sticky='nsew')
                        self.frames[frame.__class__.__name__] = frame

    # Changing the view through ID's we input
    def change_view(self, cont):
        self.nav_bar.active_btn()
        frame = self.frames[cont]
        frame.tkraise()
