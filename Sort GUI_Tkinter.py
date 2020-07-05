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


# -------------------------  Sort fuction  --------------------------
#####################################################################
def bubble_sort():
    global data, LATE
    
    startTime = time.time()
    length = data[1] - 1
    for i in range(length) :
        for j in range(length-i) :
            time.sleep(LATE)
            if data[0][j] > data[0][j+1] :
                data[0][j], data[0][j+1] = data[0][j+1], data[0][j]

            rectangle_list = MakeRectangle(data)
            canvas.update()
            canvas.delete("all")
            drawRectangle(rectangle_list) 
            changeDataColor_Red(rectangle_list, j)
            
            for k in range(data[1]-i, data[1]) :
                changeDataColor_Green(rectangle_list, k)
    
    for k in range(data[1]) :
        changeDataColor_Green(rectangle_list, k)
    
    # text 출력
    finishedTime = time.time()
    runtime = finishedTime - startTime

    text.insert(INSERT, "--------------------------------")    
    text.insert(INSERT, "\nbubble sort")
    
    txt = "\nn : " + str(data[1])
    text.insert(INSERT,txt)
    
    txt = "\nruntime : " + str(runtime)
    text.insert(INSERT, txt)
    text.insert(INSERT, "\n--------------------------------\n")



#####################################################################
def insertion_sort():
    global data, LATE
    startTime = time.time()
    
    for i in range(1, data[1]) :
        for j in range(i, 0, -1) :
            time.sleep(LATE)
            
            if data[0][j] < data[0][j-1] :
                data[0][j], data[0][j-1] = data[0][j-1], data[0][j]
            else : 
                break
            
            rectangle_list = MakeRectangle(data)
            canvas.update()
            canvas.delete("all")
            drawRectangle(rectangle_list) 
            
            changeDataColor_Red(rectangle_list, j)


    # text 출력
    finishedTime = time.time()
    runtime = finishedTime - startTime

    text.insert(INSERT, "--------------------------------")    
    text.insert(INSERT, "\ninsertion sort")
    
    txt = "\nn : " + str(data[1])
    text.insert(INSERT,txt)
    
    txt = "\nruntime : " + str(runtime)
    text.insert(INSERT, txt)
    text.insert(INSERT, "\n--------------------------------\n") 

#####################################################################
def selection_sort():
    global data
    startTime = time.time()
    
    for i in range(data[1]-1):
        min_index = i
        # 최소값 찾는 처리
        for k in range(i+1, data[1]):
            if data[0][k] < data[0][min_index]:
                min_index = k
                
                rectangle_list = MakeRectangle(data)
                canvas.update()
                canvas.delete("all")
                drawRectangle(rectangle_list)
                changeDataColor_Red(rectangle_list, k)
                for l in range(i) :
                    changeDataColor_Green(rectangle_list, l)


        # 최소값의 위치를 바꿔주는 처리
        data[0][i], data[0][min_index] = data[0][min_index], data[0][i]

        rectangle_list = MakeRectangle(data)
        canvas.update()
        canvas.delete("all")
        drawRectangle(rectangle_list)
        for l in range(i+2) :
            changeDataColor_Green(rectangle_list, l)
        
    # text 출력
    finishedTime = time.time()
    runtime = finishedTime - startTime

    text.insert(INSERT, "--------------------------------")    
    text.insert(INSERT, "\nselection sort")
    
    txt = "\nn : " + str(data[1])
    text.insert(INSERT,txt)
    
    txt = "\nruntime : " + str(runtime)
    text.insert(INSERT, txt)
    text.insert(INSERT, "\n--------------------------------\n") 
        
#####################################################################
def shell_sort():
    global data
    startTime = time.time()
    
    size = data[1]
    gap = size//2
    
    while gap > 0 :
        for i in range(gap,size):
            temp=data[0][i]
            j = i
            
            while j >= gap and data[0][j-gap] > temp:
                data[0][j] = data[0][j-gap]
                j -= gap
            data[0][j] = temp
            
            rectangle_list = MakeRectangle(data)
            canvas.update()
            canvas.delete("all")
            drawRectangle(rectangle_list)
            changeDataColor_Red(rectangle_list, j)
            
        gap //= 2


    # text 출력
    finishedTime = time.time()
    runtime = finishedTime - startTime

    text.insert(INSERT, "--------------------------------")    
    text.insert(INSERT, "\nshell sort")
    
    txt = "\nn : " + str(data[1])
    text.insert(INSERT,txt)
    
    txt = "\nruntime : " + str(runtime)
    text.insert(INSERT, txt)
    text.insert(INSERT, "\n--------------------------------\n") 
    
#####################################################################        
def quick_sort():
    global data
    startTime = time.time()
    
    def quick_sort_internal(start, end):
        if start >= end : 
            return
        pivot = data[0][end]
        l, r = start, end-1
        
        while l <= r:
            if data[0][r] < pivot < data[0][l]:
                data[0][l], data[0][r] = data[0][r], data[0][l]
                
            if data[0][l] < pivot :
                l += 1
            if data[0][r] > pivot : 
                r -= 1
        
            rectangle_list = MakeRectangle(data)
            canvas.update()
            canvas.delete("all")
            drawRectangle(rectangle_list)
            
            changeDataColor_Red(rectangle_list, l)
            changeDataColor_Red(rectangle_list, r)
            
        data[0][end] = data[0][l]
        data[0][l] = pivot


        rectangle_list = MakeRectangle(data)
        canvas.update()
        canvas.delete("all")
        drawRectangle(rectangle_list)
         
        
        quick_sort_internal(start, l-1)
        quick_sort_internal(l+1, end)

    quick_sort_internal(0, data[1]-1)


    # text 출력
    finishedTime = time.time()
    runtime = finishedTime - startTime

    text.insert(INSERT, "--------------------------------")    
    text.insert(INSERT, "\nquick sort")
    
    txt = "\nn : " + str(data[1])
    text.insert(INSERT,txt)
    
    txt = "\nruntime : " + str(runtime)
    text.insert(INSERT, txt)
    text.insert(INSERT, "\n--------------------------------\n") 
    
##################################################################### 
def merge_sort():
    global data
    startTime = time.time()
    
    def merge(left, mid, right):
        i, j = 0, 0
        P = [0]*(right-left)
        while i+j < right-left :
            if j == right-mid or (i < mid-left and data[0][left+i] < data[0][mid+j]):
                P[i+j] = data[0][left+i]
                i += 1
            else :
                P[i+j] = data[0][mid+j]
                j += 1
        for k in range(right-left) :
            data[0][left + k] = P[k]
        
            rectangle_list = MakeRectangle(data)
            canvas.update()
            canvas.delete("all")
            drawRectangle(rectangle_list)
            changeDataColor_Red(rectangle_list, left+k)
            
    def merge_sort_internal(left, right):
        if right - left < 2: return
        mid = (right + left) // 2
        merge_sort_internal(left, mid)
        merge_sort_internal(mid, right)
        merge(left, mid, right)

    merge_sort_internal(0, data[1])


    # text 출력
    finishedTime = time.time()
    runtime = finishedTime - startTime

    text.insert(INSERT, "--------------------------------")    
    text.insert(INSERT, "\nmerge sort")
    
    txt = "\nn : " + str(data[1])
    text.insert(INSERT,txt)
    
    txt = "\nruntime : " + str(runtime)
    text.insert(INSERT, txt)
    text.insert(INSERT, "\n--------------------------------\n") 
    
##################################################################### 
def heap_sort():
    global data
    startTime = time.time()
    
    n = data[1]
    for i in range(n // 2 - 1, -1, -1):
        heapify(i, n)
        
    for i in range(n - 1, 0, -1):
        data[0][0], data[0][i] = data[0][i], data[0][0]
        heapify(0, i)

    # text 출력
    finishedTime = time.time()
    runtime = finishedTime - startTime

    text.insert(INSERT, "--------------------------------")    
    text.insert(INSERT, "\nheap sort")
    
    txt = "\nn : " + str(data[1])
    text.insert(INSERT,txt)
    
    txt = "\nruntime : " + str(runtime)
    text.insert(INSERT, txt)
    text.insert(INSERT, "\n--------------------------------\n")


def heapify(index, size):
    global data
    
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    
    if left_index < size and data[0][left_index] > data[0][largest]:
        largest = left_index
    if right_index < size and data[0][right_index] > data[0][largest]:
        largest = right_index
    if largest != index:
        data[0][largest], data[0][index] = data[0][index], data[0][largest]
        
        rectangle_list = MakeRectangle(data)
        canvas.update()
        canvas.delete("all")
        drawRectangle(rectangle_list)
        
        heapify(largest, size)  
    
    
 

##################################################################### 
        
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
    global data
    
    if value1.get() == 0 :
        messagebox.showinfo("Error", "Please choose sort!")
    elif value1.get() == 1 :
        bubble_sort()
    elif value1.get() == 2 :
        insertion_sort()
    elif value1.get() == 3 :
        selection_sort()
    elif value1.get() == 4 :
        shell_sort()
    elif value1.get() == 5 :
        quick_sort()
    elif value1.get() == 6 :
        merge_sort()
    elif value1.get() == 7 :
        heap_sort()
    elif value1.get() == 8 :
        radix_sort()


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