import tkinter as tk

class network_menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, height = 250, bg='blue')
        tk.Label(self, text="Network_menu", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        