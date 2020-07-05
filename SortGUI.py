# -*- coding: utf-8 -*-
'''
Data Structure Sort GUI
made by 19-079 이지원

Sort index
1. Bubble sort
2. Insertion sort
3. Selection sort
4. Shell sort
5. Quick sort
6. Merge sort
7. Heap sort
8. Radix sort

'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import random

# -----------------------------  GUI  ------------------------------
# 기본
root = Tk()

root.title("Sort GUI")
root.geometry("850x600+10+50")
#root.geometry("850x600+100+100")
root.resizable(False, False)


#####################################################################
# data가 주어지면 list로 만들어주는 fuction
def MakeList(n) :
    list = []
    for i in range(n) :
        list.append(400*(i+1)/n)
    return [list, n]

def MakeRectangle(data) :
    list = []
    n = data[1]
    for i in range(data[1]) :
        list.append([600*i/n, 400-data[0][i], 600*(i+1)/n, 400])
    return list

# data가 주어지면 그려줌
def drawRectangle(list) :
    for i in range(len(list)) :
        canvas.create_rectangle(list[i][0], list[i][1], list[i][2], list[i][3], fill="white")


# data[i]의 색을 빨간색으로 바꿈
def changeDataColor_Red(list, i) :
    canvas.create_rectangle(list[i][0], list[i][1], list[i][2], list[i][3], fill="red")

def changeDataColor_Green(list, i) :
    canvas.create_rectangle(list[i][0], list[i][1], list[i][2], list[i][3], fill="green")

def changeDataColor_Yellow(list, i) :
    canvas.create_rectangle(list[i][0], list[i][1], list[i][2], list[i][3], fill="yellow")

##################################################################### 
# canvas
canvas = Canvas(root, width=600, height=400, bg = "black", bd=2)
canvas.place(x=20,y=20)

canvas.create_rectangle(0,0,600,400, fill="yellow")


#####################################################################
# spinBox
label_data=Label(root, text="data 개수(1~300)")
label_data.place(x=650,y=20)

def value_check(self):
    global data
    label_data.config(text="data 개수(1~300)")
    valid = False
    if self.isdigit():
        if (int(self) <= 10000 and int(self) >= 1):
            valid = True
            
            # canvas에 그리기
            n = int(self)
            data = MakeList(n)
            rectangle_list = MakeRectangle(data)
            canvas.delete("all")
            drawRectangle(rectangle_list)
            
    elif self == '':
        valid = True
    return valid

def value_error(self):
    label_data.config(text=str(self) + "를 입력하셨습니다.\n올바른 값을 입력하세요.")

validate_command = (root.register(value_check), '%P')
invalid_command = (root.register(value_error), '%P')

spinbox_dataNum = Spinbox(root, from_ = 1, to = 10000, validate = 'all', validatecommand = validate_command, invalidcommand=invalid_command)
spinbox_dataNum.place(x=650,y=60)

#####################################################################
# spinBox
label_speed=Label(root, text="speed(1~10)")
label_speed.place(x=650,y=100)


def value_check_speed(self):
    global LATE
    
    label_speed.config(text="speed(1~10)")
    valid = False
    if self.isdigit():
        if (int(self) <= 10 and int(self) >= 1):
            valid = True
            LATE = 0.01*(10-int(self))
            
    elif self == '':
        valid = True
    return valid

def value_error_speed(self):
    label_speed.config(text=str(self) + "를 입력하셨습니다.\n올바른 값을 입력하세요.")

validate_command = (root.register(value_check_speed), '%P')
invalid_command = (root.register(value_error_speed), '%P')

spinbox_LATE = Spinbox(root, from_ = 1, to = 10, validate = 'all', validatecommand = validate_command, invalidcommand=invalid_command)
spinbox_LATE.place(x=650,y=140)

############################################################

# function
def suffle_list() :
    global data
    canvas.delete("all")
    
    
    n = int(spinbox_dataNum.get())
    data = MakeList(n)
    random.shuffle(data[0])
    rectangle_list = MakeRectangle(data)
    canvas.delete("all")
    drawRectangle(rectangle_list)

##############################################################3
def sort_list() :
    global data, LATE
    
    if value1.get() == 0 :
        messagebox.showinfo("Error", "Please choose sort!")
    elif value1.get() == 1 :
        bubble_sort(data, LATE)
    elif value1.get() == 2 :
        insertion_sort(data, LATE)
    elif value1.get() == 3 :
        selection_sort(data, LATE)
    elif value1.get() == 4 :
        shell_sort(data, LATE)
    elif value1.get() == 5 :
        quick_sort(data, LATE)
    elif value1.get() == 6 :
        merge_sort(data, LATE)
    elif value1.get() == 7 :
        heap_sort(data, LATE)
    elif value1.get() == 8 :
        radix_sort(data, LATE)


#####################################################################
# suffle, sort button
btn_suffle = Button(root, text="Suffle", command=suffle_list)
btn_sort = Button(root, text="Sort", command=sort_list)

btn_suffle.place(x=650,y=400)
btn_sort.place(x=750,y=400)

#####################################################################
# sort Radio button / 7개
value1 = IntVar()

bt_1 = Radiobutton(root, text="Bubble sort", value = 1, variable = value1)
bt_2 = Radiobutton(root, text="Insertion sort", value = 2, variable = value1)
bt_3 = Radiobutton(root, text="Selection sort", value = 3, variable = value1)
bt_4 = Radiobutton(root, text="Shell sort", value = 4, variable = value1)
bt_5 = Radiobutton(root, text="Quick sort", value = 5, variable = value1)
bt_6 = Radiobutton(root, text="Merge sort", value = 6, variable = value1)
bt_7 = Radiobutton(root, text="Heap sort", value = 7, variable = value1)

bt_1.place(x=650,y=200)
bt_2.place(x=750,y=200)
bt_3.place(x=650,y=250)
bt_4.place(x=750,y=250)
bt_5.place(x=650,y=300)
bt_6.place(x=750,y=300)
bt_7.place(x=650,y=350)


#####################################################################
# text
text = Text(root, width=110, height=10)
text.place(x=20,y=450)


root.mainloop()