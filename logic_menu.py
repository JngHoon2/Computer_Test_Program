import tkinter
import tkinter as tk
import time
import tkinter.messagebox

class logic_menu(tk.Frame):

    value_1 = False     #
    value_2 = False     #
    value_3 = False     ## definition of input_value, default is false
    value_4 = False     #
    value_5 = False     #

    result_and = False  #
    result_nand = False #
    result_or = False   ## definition of logic_value, default is false
    result_nor = False  #
    result_xor = False  #
    result_xnor = False #

    ################################################ OVERRIDING ################################################
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, width = 640, height = 250)
        tk.Label(self, text = 'input 수량을 선택하세요.', width = 20).place(x = 230, y = 5)


        ########################## GIF Setting ##########################
        gf_GTR = [tkinter.PhotoImage(file='/Users/tuan/Documents/Data/Image_Data/toggle_Green_to_Red_64x64.gif', 
                            format = 'gif -index %i' %i) for i in range(23)]

        gf_RTG = [tkinter.PhotoImage(file='/Users/tuan/Documents/Data/Image_Data/toggle_Red_to_Green_64x64.gif', 
                            format = 'gif -index %i' %i) for i in range(23)]

        def function_GTR(toggleNum):
            for index in range(23):
                frame = gf_GTR[index]
                index += 1
                image_input[toggleNum].configure(image=frame)
                self.update()
                time.sleep(0.001)
                

        def function_RTG(toggleNum):
            for index in range(23):
                frame = gf_RTG[index]
                index += 1
                image_input[toggleNum].configure(image=frame)
                self.update()
                time.sleep(0.001)
        ########################## GIF Setting ##########################

        ############################# Calculate Logic & Chage Result #############################
        def change_result():

            if vInput.get() == 2:
                self.result_and = self.value_1 and self.value_2
                self.result_nand = not self.result_and
                self.result_or = self.value_1 or self.value_2
                self.result_nor = not self.result_or
                self.result_xor = self.value_1 ^ self.value_2
                self.result_xnor = not self.result_xor
            if vInput.get() == 3:
                self.result_and = self.value_1 and self.value_2 and self.value_3
                self.result_nand = not self.result_and
                self.result_or = self.value_1 or self.value_2 or self.value_3 
                self.result_nor = not self.result_or
                self.result_xor = self.value_1 ^ self.value_2 ^ self.value_3
                self.result_xnor = not self.result_xor
            if vInput.get() == 4:
                self.result_and = self.value_1 and self.value_2 and self.value_3 and self.value_4
                self.result_nand = not self.result_and
                self.result_or = self.value_1 or self.value_2 or self.value_3 or self.value_4
                self.result_nor = not self.result_or
                self.result_xor = self.value_1 ^ self.value_2 ^ self.value_3 ^ self.value_4
                self.result_xnor = not self.result_xor
            if vInput.get() == 5:
                self.result_and = self.value_1 and self.value_2 and self.value_3 and self.value_4 and self.value_5
                self.result_nand = not self.result_and
                self.result_or = self.value_1 or self.value_2 or self.value_3 or self.value_4 or self.value_5
                self.result_nor = not self.result_or
                self.result_xor = self.value_1 ^ self.value_2 ^ self.value_3 ^ self.value_4 ^ self.value_5
                self.result_xnor = not self.result_xor
                

            # And_logic result setting
            if self.result_and == True:
                result_img_and.configure(image = result_img_true)
            else:
                result_img_and.configure(image = result_img_false)
            
            # Nand_logic result setting
            if self.result_nand == True:
                result_img_nand.configure(image = result_img_true)
            else:
                result_img_nand.configure(image = result_img_false)

            # OR_logic result setting
            if self.result_or == True:
                result_img_or.configure(image = result_img_true)
            else:
                result_img_or.configure(image = result_img_false)

            # Nor_logic result setting
            if self.result_nor == True:
                result_img_nor.configure(image = result_img_true)
            else:
                result_img_nor.configure(image = result_img_false)

            # Xor_logic result setting
            if self.result_xor == True:
                result_img_xor.configure(image = result_img_true)
            else:
                result_img_xor.configure(image = result_img_false)

            # Xnor_logic result setting
            if self.result_xnor == True:
                result_img_xnor.configure(image = result_img_true)
            else:
                result_img_xnor.configure(image = result_img_false)

        ############################# Calculate Logic & Chage Result #############################

        ####################### Calculate Logic & Chage Result #######################
        def click_toggle_1(event):
            if self.value_1 == False:
                self.value_1 = True
                function_RTG(0)
            else:
                self.value_1 = False
                function_GTR(0)

            change_result()

        def click_toggle_2(event):
            if self.value_2 == False:
                self.value_2 = True
                function_RTG(1)
            else:
                self.value_2 = False
                function_GTR(1)

            change_result()

        def click_toggle_3(event):
            if self.value_3 == False:
                self.value_3 = True
                function_RTG(2)
            else:
                self.value_3 = False
                function_GTR(2)
            
            change_result()

        def click_toggle_4(event):
            if self.value_4 == False:
                self.value_4 = True
                function_RTG(3)
            else:
                self.value_4 = False
                function_GTR(3)

            change_result()

        def click_toggle_5(event):
            if self.value_5 == False:
                self.value_5 = True
                function_RTG(4)
            else:
                self.value_5 = False
                function_GTR(4)
            
            change_result()
        ####################### Calculate Logic & Chage Result #######################

        ####################  Definition of Make toggle button By radio button ####################
        def click_input_2():
            image_input_1.place(x = 170, y = 60)
            image_input_2.place(x = 406, y = 60)
            image_input_3.place_forget()            ## Make 2 Buttons ##
            image_input_4.place_forget()
            image_input_5.place_forget()
            self.update()

        def click_input_3():
            image_input_1.place(x = 112, y = 60)
            image_input_2.place(x = 288, y = 60)
            image_input_3.place(x = 464, y = 60)    ## Make 3 Buttons ##
            image_input_4.place_forget()
            image_input_5.place_forget()

        def click_input_4():
            image_input_1.place(x = 76, y = 60)
            image_input_2.place(x = 216, y = 60)
            image_input_3.place(x = 360, y = 60)    ## Make 4 Buttons ##
            image_input_4.place(x = 500, y = 60)
            image_input_5.place_forget()

        def click_input_5():
            image_input_1.place(x = 32, y = 60)
            image_input_2.place(x = 160, y = 60)
            image_input_3.place(x = 288, y = 60)    ## Make 5 Buttons ##
            image_input_4.place(x = 416, y = 60)
            image_input_5.place(x = 544, y = 60)
        ####################  Definition of Make toggle button By radio button ####################

        ####################### Radio Button Setting #######################
        vInput = tkinter.IntVar()

        radio_input_2 = tk.Radiobutton(self, text = '2 input', value = 2, variable = vInput, command = click_input_2)
        radio_input_3 = tk.Radiobutton(self, text = '3 input', value = 3, variable = vInput, command = click_input_3)
        radio_input_4 = tk.Radiobutton(self, text = '4 input', value = 4, variable = vInput, command = click_input_4)
        radio_input_5 = tk.Radiobutton(self, text = '5 input', value = 5, variable = vInput, command = click_input_5)

        radio_input_2.place(x = 120, y = 40)
        radio_input_3.place(x = 240, y = 40)
        radio_input_4.place(x = 360, y = 40)
        radio_input_5.place(x = 480, y = 40)

        radio_input_2.invoke()    ## default check setting ##
        
        ####################### Radio Button Setting #######################

        ####################### Toggle Button Setting #######################
        toggleImg_Green = tkinter.PhotoImage(file = '/Users/tuan/Documents/Data/Image_Data/toggle_Green_to_Red_64x64.gif')
        toggleImg_Red = tkinter.PhotoImage(file = '/Users/tuan/Documents/Data/Image_Data/toggle_Red_to_Green_64x64.gif')

        image_input_1 = tk.Label(self, image = toggleImg_Red)
        image_input_2 = tk.Label(self, image = toggleImg_Red)
        image_input_3 = tk.Label(self, image = toggleImg_Red)
        image_input_4 = tk.Label(self, image = toggleImg_Red)
        image_input_5 = tk.Label(self, image = toggleImg_Red)

        image_input = [image_input_1, image_input_2, image_input_3, image_input_4, image_input_5]

        image_input_1.bind('<Button-1>', click_toggle_1)
        image_input_2.bind('<Button-1>', click_toggle_2)
        image_input_3.bind('<Button-1>', click_toggle_3)
        image_input_4.bind('<Button-1>', click_toggle_4)
        image_input_5.bind('<Button-1>', click_toggle_5)

        image_input_1.place(x = 170, y = 60)        ## default image setting ##
        image_input_2.place(x = 406, y = 60)
         ####################### Toggle Button Setting #######################

         ####################### Result section #######################
        lblAnd = tkinter.Label(self, text = 'AND', width=10, height=1)
        lblNand = tkinter.Label(self, text = 'NAND', width=10, height=1)
        lblOr = tkinter.Label(self, text = 'OR', width=10, height=1)
        lblNor = tkinter.Label(self, text = 'NOR', width=10, height=1)
        lblXor = tkinter.Label(self, text = 'XOR', width=10, height=1)
        lblXnor = tkinter.Label(self, text = 'XNOR', width=10, height=1)

        lblAnd.place(x = 36 , y = 140)
        lblNand.place(x = 132 , y = 140)
        lblOr.place(x = 228 , y = 140)
        lblNor.place(x = 322, y = 140)
        lblXor.place(x = 418, y = 140)
        lblXnor.place(x = 514, y = 140)

        result_img_true = tkinter.PhotoImage(file = '/Users/tuan/Documents/Data/Image_Data/green_light_64x64.png')
        result_img_false = tkinter.PhotoImage(file = '/Users/tuan/Documents/Data/Image_Data/red_light_64x64.png') 

        result_img_and = tkinter.Label(self, image = result_img_false)
        result_img_nand = tkinter.Label(self, image = result_img_true)
        result_img_or = tkinter.Label(self, image = result_img_false)
        result_img_nor = tkinter.Label(self, image = result_img_true)
        result_img_xor = tkinter.Label(self, image = result_img_false)
        result_img_xnor = tkinter.Label(self, image = result_img_true)

        result_img_and.place(x = 50, y = 160)       #
        result_img_nand.place(x = 145, y = 160)     #
        result_img_or.place(x = 241, y = 160)       #
        result_img_nor.place(x = 336, y = 160)      ## default image setting
        result_img_xor.place(x = 432, y = 160)      #
        result_img_xnor.place(x = 528, y = 160)     #
        ####################### REsult section #######################

    ################################################ OVERRIDING ################################################
    

        
        