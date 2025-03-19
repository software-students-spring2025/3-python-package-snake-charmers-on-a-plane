import tkinter as tk
from tkinter import ttk

class Settings(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Settings")
        self.geometry("300x200")
        #  settings
        self.settings = {
            "speed": tk.IntVar(value=50)
        }
        # Speed
        ttk.Label(self, text="Enter speed (1-100):").pack(pady=5)
        self.speed_entry = ttk.Entry(self, textvariable=self.settings["speed"])
        self.speed_entry.pack()
        # button
        self.start_button = tk.Button(self, text="Start", command=self.apply_settings, bg="lightgray", fg="black")
        self.start_button.pack(pady=10)

    def apply_settings(self):
        ''''self.master.settings = {
            "speed": max(1, min(100, self.settings["speed"].get()))
        }
        self.destroy()'''
        # this should be better
        for key in self.settings:
            self.master.settings[key] = self.settings[key].get()
        self.destroy()