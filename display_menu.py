import tkinter as tk

class display_menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, height = 250, bg='blue')
        tk.Label(self, text="Display_menu", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        