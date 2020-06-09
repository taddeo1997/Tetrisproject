#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:43:31 2020

@author: lucatoscano
"""

import tkinter as tk


#create the window
window= tk.Tk()
 
#size of window
window.geometry ('500x500+500+700') #width, height, coordinate x and y (pixel)

#title of window
window.title("my first window")

#adding test
text=tk.Label(window,text="TETRIS",fg="blue",bg="green",font=("Helvetica",27)).pack()  #pack method places text in central position

#function of the botton
def button1_function():
    button_text=tk.Label(window,text="the button work well").pack()

#add botton
button1=tk.Button(window,text="unuseful",command=button1_function).pack()


#start the main loop
window.mainloop()