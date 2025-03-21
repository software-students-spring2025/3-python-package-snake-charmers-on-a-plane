import tkinter as tk
from tkinter import ttk

class Settings(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Settings")
        self.geometry("250x200")
        #Settings

        #Speed
        self.settings = {
            "speed": tk.IntVar(value=50)
        }
    
        ttk.Label(self, text="Enter speed (1-100):").pack(pady=5)
        self.speed_entry = ttk.Entry(self, textvariable=self.settings["speed"])
        self.speed_entry.pack()

        #Color
        self.color_settings = {
            "color" : tk.StringVar(value = "yellow")
        }

        ttk.Label(self, text="Enter a color. Invalid colors will be randomized!").pack(pady=10)
        self.color_entry = ttk.Entry(self, textvariable = self.color_settings["color"])
        self.color_entry.pack()

        # button
        self.start_button = tk.Button(self, text="Start", command=self.apply_settings, bg="lightgray", fg="black")
        self.start_button.pack(pady=15)

        

    def apply_settings(self):
        # this should be better
        for key in self.settings:
            self.master.settings[key] = self.settings[key].get()
        for key in self.color_settings:
            self.master.color_settings[key] = self.color_settings[key].get()
            print("in settings:", self.master.color_settings[key])
        self.destroy()

    """
    pipfile you write
    pipfile.lock is generated from that with pipenv install
    """
    # possible options:
    # create a new env and then run your package in there -- use the errors to pipenv install those packages
    # write requirements.txt -> use that to generate pipfile(.lock?)
    # ask if no one has (base) / no conda

    # no module named _tkinter 

    """
    properly:
    virtualenv 
    nav to your package
    pipenv install
    pipfile should be generated from this!
    yes make sure your pipenv has all the libraries etc you need including pytest
    and tkinter etc

    after generate pipfile and pipfile.loc,
    pipenv shell to activate environment
    run pytest
    make sure to try tunning unit tests in this env too

    and then use pipenv install package_name etc

    PIL is now called pillow, so install that

    more now a unit test issue than anything pipfile related, just write that pipfile ig

    look at other ppls pipfile

    should rename snakecharmerpackage randomsnake or something if you want it to be randomsnake

    yay it's not a pipfile issue really

    """