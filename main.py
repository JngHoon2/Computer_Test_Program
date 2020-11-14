import tkinter
import home
from home import BassApp

MainWindow = BassApp()
MainWindow.title('Computer Testing Program(가제)')
MainWindow.geometry('640x300+400+200')
MainWindow.resizable(False, False)

MainWindow.mainloop()