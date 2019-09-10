from tkinter import *
import parsing
import numpy as np
import copy as cp

def add_to_cart(window, item, count):
    if (item[3] == 0):
        count[0] += 1
        lbl = Label(window, text = item[0] + " x " + str(item[3]) + " = " + "{:.2f}".format(float(item[1]) * item[3]) + "€")
        lbl.grid(column = 0, row = 3 + count[0])
    item[3] += 1


def checkout(data, window):
    price = 0
    i=0
    for item in data:
        price += float(item[1]) * item[3]
    lbl = Label(window, text = "Total: " + "{:.2f}".format(price) + "€")
    lbl.grid(column = 2, row = 4)
    btn = Button(window, text = "Back", command = (lambda : start(window)))
    btn.grid(column = 2, row = 5)

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def erase(window):
    L = all_children(window)
    for x in L:
        x.destroy()

def start(window):
    erase(window)
    lbl = Label(window, text="Choose an item")
    lbl.grid(column=0, row=0)
    data = parsing.get_file("KFETitems.txt")
    i = 0
    count = [0]
    def toto(i):
        btn = Button(window, text = data[i][0], command = (lambda : add_to_cart(window, data[i], count)))
        btn.grid(column = 2 * (i // 3), row = i % 3 + 1)
        lbl = Label(window, text = data[i][1] + "€")
        lbl.grid(column = 2 * (i // 3) + 1, row = i % 3 + 1)
    for i in range(len(data)):
        toto(i)
    btn = Button(window, text = "Checkout", command =(lambda : checkout(data, window)))
    i+=1
    btn.grid(column = 2 * (i // 3) + 1, row = 3)

def main():
    master = Tk()
    master.title("Bienvenue a la KFET")
    master.geometry('300x200')
    start(master)
    master.mainloop()






