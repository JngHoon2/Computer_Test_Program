import tkinter
import time
### 윈도우 세팅 ###
LogicWindow = tkinter.Tk()

LogicWindow.title('Computer Testing Program(가제)')
LogicWindow.geometry('640x300+400+200')
LogicWindow.resizable(False, False)
### 윈도우 세팅 ###

frameLogic=tkinter.Frame( relief="ridge", bd=1, height = 250)
frameLogic.pack(side="top", fill="both", expand = True)

### endline 표시용 ###
# frameMenu=tkinter.Frame(LogicWindow, relief="ridge", bd=1, height = 50)
# frameMenu.pack(side="bottom", fill="both", expand = True)
# lbl = tkinter.Label(frameMenu, text = 'EndLine')
# lbl.place(x = 0, y = 0)
### endline 표시용 ###


lbl = tkinter.Label(frameLogic, text = 'input 수량을 선택하세요.', width=20, height=1)
lbl.place(x = 230 , y = 5)


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

### GIF Setting ###

gf_GTR = [tkinter.PhotoImage(file='/Users/tuan/Documents/Data/Image_Data/toggle_Green_to_Red_64x64.gif', 
                    format = 'gif -index %i' %i) for i in range(23)]

gf_RTG = [tkinter.PhotoImage(file='/Users/tuan/Documents/Data/Image_Data/toggle_Red_to_Green_64x64.gif', 
                    format = 'gif -index %i' %i) for i in range(23)]

def function_GTR(toggleNum):
    for index in range(23):
        frame = gf_GTR[index]
        index += 1
        image_input[toggleNum].configure(image=frame)
        frameLogic.update()
        time.sleep(0.001)
        

def function_RTG(toggleNum):
    for index in range(23):
        frame = gf_RTG[index]
        index += 1
        image_input[toggleNum].configure(image=frame)
        frameLogic.update()
        time.sleep(0.001)

### GIF Setting ###

### Calculate Logic & Chage Result ###
def change_result():
    global result_and  
    global result_nand 
    global result_or    
    global result_nor  
    global result_xor  
    global result_xnor 

    if vInput.get() == 2:
        result_and = value_1 and value_2
        result_nand = not result_and
        result_or = value_1 or value_2
        result_nor = not result_or
        result_xor = value_1 ^ value_2
        result_xnor = not result_xor
    if vInput.get() == 3:
        result_and = value_1 and value_2 and value_3
        result_nand = not result_and
        result_or = value_1 or value_2 or value_3 
        result_nor = not result_or
        result_xor = value_1 ^ value_2 ^ value_3
        result_xnor = not result_xor
    if vInput.get() == 4:
        result_and = value_1 and value_2 and value_3 and value_4
        result_nand = not result_and
        result_or = value_1 or value_2 or value_3 or value_4
        result_nor = not result_or
        result_xor = value_1 ^ value_2 ^ value_3 ^ value_4
        result_xnor = not result_xor
    if vInput.get() == 5:
        result_and = value_1 and value_2 and value_3 and value_4 and value_5
        result_nand = not result_and
        result_or = value_1 or value_2 or value_3 or value_4 or value_5
        result_nor = not result_or
        result_xor = value_1 ^ value_2 ^ value_3 ^ value_4 ^ value_5
        result_xnor = not result_xor
        

    # And_logic result setting
    if result_and == True:
        result_img_and.configure(image = result_img_true)
    else:
        result_img_and.configure(image = result_img_false)
    
    # Nand_logic result setting
    if result_nand == True:
        result_img_nand.configure(image = result_img_true)
    else:
        result_img_nand.configure(image = result_img_false)

    # OR_logic result setting
    if result_or == True:
        result_img_or.configure(image = result_img_true)
    else:
        result_img_or.configure(image = result_img_false)

    # Nor_logic result setting
    if result_nor == True:
        result_img_nor.configure(image = result_img_true)
    else:
        result_img_nor.configure(image = result_img_false)

    # Xor_logic result setting
    if result_xor == True:
        result_img_xor.configure(image = result_img_true)
    else:
        result_img_xor.configure(image = result_img_false)

    # Xnor_logic result setting
    if result_xnor == True:
        result_img_xnor.configure(image = result_img_true)
    else:
        result_img_xnor.configure(image = result_img_false)

### Calculate Logic & Chage Result ###


def click_toggle_1(event):
    global value_1      ## 전역 변수 value 사용 
    if value_1 == False:
        value_1 = True
        function_RTG(0)
    else:
        value_1 = False
        function_GTR(0)

    change_result()
    frameLogic.update()

def click_toggle_2(event):
    global value_2
    if value_2 == False:
        value_2 = True
        function_RTG(1)
    else:
        value_2 = False
        function_GTR(1)

    change_result()
    frameLogic.update()

def click_toggle_3(event):
    global value_3
    if value_3 == False:
        value_3 = True
        function_RTG(2)
    else:
        value_3 = False
        function_GTR(2)
    
    change_result()
    frameLogic.update()

def click_toggle_4(event):
    global value_4
    if value_4 == False:
        value_4 = True
        function_RTG(3)
    else:
        value_4 = False
        function_GTR(3)

    change_result()
    frameLogic.update()

def click_toggle_5(event):
    global value_5
    if value_5 == False:
        value_5 = True
        function_RTG(4)
    else:
        value_5 = False
        function_GTR(4)
    
    change_result()
    frameLogic.update()


### toggle switch ###
toggleImg_Green = tkinter.PhotoImage(file = '/Users/tuan/Documents/Data/Image_Data/toggle_Green_to_Red_64x64.gif')
toggleImg_Red = tkinter.PhotoImage(file = '/Users/tuan/Documents/Data/Image_Data/toggle_Red_to_Green_64x64.gif')

image_input_1 = tkinter.Label(frameLogic, image = toggleImg_Red)
image_input_2 = tkinter.Label(frameLogic, image = toggleImg_Red)
image_input_3 = tkinter.Label(frameLogic, image = toggleImg_Red)
image_input_4 = tkinter.Label(frameLogic, image = toggleImg_Red)
image_input_5 = tkinter.Label(frameLogic, image = toggleImg_Red)

image_input = [image_input_1, image_input_2, image_input_3, image_input_4, image_input_5]

image_input_1.bind('<Button-1>', click_toggle_1)
image_input_2.bind('<Button-1>', click_toggle_2)
image_input_3.bind('<Button-1>', click_toggle_3)
image_input_4.bind('<Button-1>', click_toggle_4)
image_input_5.bind('<Button-1>', click_toggle_5)

### Radio Button ###
def click_input_2():
    image_input_1.place(x = 170, y = 60)
    image_input_2.place(x = 406, y = 60)
    image_input_3.place_forget()            ### 버튼 2개 생성 ###
    image_input_4.place_forget()
    image_input_5.place_forget()
    frameLogic.update()

def click_input_3():
    image_input_1.place(x = 112, y = 60)
    image_input_2.place(x = 288, y = 60)
    image_input_3.place(x = 464, y = 60)    ### 버튼 3개 생성 ###
    image_input_4.place_forget()
    image_input_5.place_forget()
    frameLogic.update()

def click_input_4():
    image_input_1.place(x = 76, y = 60)
    image_input_2.place(x = 216, y = 60)
    image_input_3.place(x = 360, y = 60)    ### 버튼 4개 생성 ###
    image_input_4.place(x = 500, y = 60)
    image_input_5.place_forget()
    frameLogic.update()

def click_input_5():
    image_input_1.place(x = 32, y = 60)
    image_input_2.place(x = 160, y = 60)
    image_input_3.place(x = 288, y = 60)    ## 버튼 5개 생성 ###
    image_input_4.place(x = 416, y = 60)
    image_input_5.place(x = 544, y = 60)
    frameLogic.update()


vInput = tkinter.IntVar()

radio_input_2 = tkinter.Radiobutton(frameLogic, text = '2 input', value = 2, variable = vInput, command = click_input_2)
radio_input_3 = tkinter.Radiobutton(frameLogic, text = '3 input', value = 3, variable = vInput, command = click_input_3)
radio_input_4 = tkinter.Radiobutton(frameLogic, text = '4 input', value = 4, variable = vInput, command = click_input_4)
radio_input_5 = tkinter.Radiobutton(frameLogic, text = '5 input', value = 5, variable = vInput, command = click_input_5)

radio_input_2.place(x = 120, y = 40)
radio_input_3.place(x = 240, y = 40)
radio_input_4.place(x = 360, y = 40)
radio_input_5.place(x = 480, y = 40)

radio_input_2.invoke()        ## default image setting

### Radio Button ###

### Result section ###

lblAnd = tkinter.Label(frameLogic, text = 'AND', width=10, height=1)
lblNand = tkinter.Label(frameLogic, text = 'NAND', width=10, height=1)
lblOr = tkinter.Label(frameLogic, text = 'OR', width=10, height=1)
lblNor = tkinter.Label(frameLogic, text = 'NOR', width=10, height=1)
lblXor = tkinter.Label(frameLogic, text = 'XOR', width=10, height=1)
lblXnor = tkinter.Label(frameLogic, text = 'XNOR', width=10, height=1)

lblAnd.place(x = 36 , y = 140)
lblNand.place(x = 132 , y = 140)
lblOr.place(x = 228 , y = 140)
lblNor.place(x = 322, y = 140)
lblXor.place(x = 418, y = 140)
lblXnor.place(x = 514, y = 140)

result_img_true = tkinter.PhotoImage(file = '/Users/tuan/Documents/Data/Image_Data/green_light_64x64.png')
result_img_false = tkinter.PhotoImage(file = '/Users/tuan/Documents/Data/Image_Data/red_light_64x64.png') 

result_img_and = tkinter.Label(frameLogic, image = result_img_false)
result_img_nand = tkinter.Label(frameLogic, image = result_img_true)
result_img_or = tkinter.Label(frameLogic, image = result_img_false)
result_img_nor = tkinter.Label(frameLogic, image = result_img_true)
result_img_xor = tkinter.Label(frameLogic, image = result_img_false)
result_img_xnor = tkinter.Label(frameLogic, image = result_img_true)

result_img_and.place(x = 50, y = 160)       #
result_img_nand.place(x = 145, y = 160)     #
result_img_or.place(x = 241, y = 160)       #
result_img_nor.place(x = 336, y = 160)      ## default image setting
result_img_xor.place(x = 432, y = 160)      #
result_img_xnor.place(x = 528, y = 160)     #

### REsult section ###

LogicWindow.mainloop()