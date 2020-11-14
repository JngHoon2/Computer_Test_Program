import tkinter
import tkinter as tk
import logic_menu
import SSD_menu
import network_menu
import display_menu

flag = [True, False, False, False, False]
class BassApp(tk.Tk):

    def switch_frame(self, frame_class):
        frameMain = frame_class(self)
        frameMain.configure(height = 250)
        if self._frame is not None:
            self._frame.destroy()

        self._frame = frameMain
        self._frame.place(x = 0, y = 0)

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

        ### Menu Frame Setting (Under_Bar) ###
        frameMenu=tkinter.Frame(relief="ridge", bd=1, height = 50)
        frameMenu.pack(side="bottom", fill="x", expand = True, anchor = 'sw')
        ### Menu Frame Setting (Under Bar) ###

        def click(event,num):
            global flag
            if flag[num] == False:
                for x in range(5):
                    flag[x] = False
                flag[num] = True
            else:
                return 
            ##############################################################################
            if flag[0] == True:
                HomeMenu.configure(bg = 'gray')
                self.switch_frame(StartPage)                    ### Go to Home ### 
            else:
                HomeMenu.configure(bg = 'white')
            ##############################################################################
            if flag[1] == True:
                LogicMenu.configure(bg = 'gray')
                self.switch_frame(logic_menu.logic_menu)        ### Go to Logic_Menu ###                 
            else:
                LogicMenu.configure(bg = 'white')
            ##############################################################################
            if flag[2] == True:
                SSDMenu.configure(bg = 'gray')
                self.switch_frame(SSD_menu.ssd_menu)            ### Go to SSD_Menu ### 
            else:
                SSDMenu.configure(bg = 'white')
            ##############################################################################
            if flag[3] == True:
                NetworkMenu.configure(bg = 'gray')
                self.switch_frame(network_menu.network_menu)    ### Go to Network_Menu ### 
            else:
                NetworkMenu.configure(bg = 'white')
            ##############################################################################
            if flag[4] == True:
                DisplayMenu.configure(bg = 'gray')
                self.switch_frame(display_menu.display_menu)    ### Go to Display_menu ### 
            else:
                DisplayMenu.configure(bg = 'white')
            ##############################################################################


        ### Menu Label Setting (Home, Logic, SSD, Nework, Display) ###
        HomeMenu = tkinter.Label(frameMenu, text = 'Home', relief = 'ridge', bg = 'gray', width = 14, height = 3)
        HomeMenu.bind('<Button-1>', lambda event, num = 0 : click(self, num))
        HomeMenu.place(x = 0, y = 0)

        LogicMenu = tkinter.Label(frameMenu, text = 'Logic', relief = 'ridge',width = 14, height = 3)
        LogicMenu.bind('<Button-1>', lambda event, num = 1 : click(self, num))
        LogicMenu.place(x = 128, y = 0)

        SSDMenu = tkinter.Label(frameMenu, text = 'SSD', relief = 'ridge',width = 14, height = 3) 
        SSDMenu.bind('<Button-1>', lambda event, num = 2 : click(self, num))
        SSDMenu.place(x = 256, y = 0)

        NetworkMenu = tkinter.Label(frameMenu, text = 'Network', relief = 'ridge',width = 14, height = 3)
        NetworkMenu.bind('<Button-1>', lambda event, num = 3 : click(self, num))
        NetworkMenu.place(x = 384, y = 0)

        DisplayMenu = tkinter.Label(frameMenu, text = 'Display', relief = 'ridge',width = 14, height = 3)
        DisplayMenu.bind('<Button-1>', lambda event, num = 4 : click(self, num))
        DisplayMenu.place(x = 512, y = 0)
        
        ### Menu Label Setting (Home, Logic, SSD, Nework, Display) ###

    

class StartPage(tk.Frame):
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, width = 640, height = 250)
        tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
                  