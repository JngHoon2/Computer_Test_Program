import tkinter as tk

class ssd_menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, height = 250, bg='blue')
        lbl = tk.Label(self, text="ssd_menu", font=('Helvetica', 18, "bold"))
        lbl.pack()

