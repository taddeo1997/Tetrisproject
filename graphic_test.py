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

#pack method places text in central position
testo1=tk.Label(window,text="TETRIS Verde",fg="black",bg="green",font=("Helvetica",27)).pack(fill=tk.X)  
testo2=tk.Label(window,text="TETRIS Bianco",fg="black",bg="white",font=("Helvetica",27)).pack(fill=tk.X)
#testo3=tk.Label(window,text="TETRIS Rosso",fg="black",bg="red",font=("Helvetica",27)).pack(fill=tk.X)  

#testo1=tk.Label(window,text="TETRIS Verde",fg="black",bg="green",font=("Helvetica",27)).grid(row=0, column=0, sticky=tk.W)  
#testo2=tk.Label(window,text="TETRIS Bianco",fg="black",bg="white",font=("Helvetica",27)).grid(row=0, column=1, sticky=tk.W)
#testo3=tk.Label(window,text="TETRIS Rosso",fg="black",bg="red",font=("Helvetica",27)).grid(row=1, column=0, sticky=tk.E)  
#testo3=tk.Label(window,text="TETRIS Blu",fg="black",bg="blue",font=("Helvetica",27)).grid(row=1, column=1, sticky=tk.E) 

#Create menu

menu_bar=tk.Menu(window).add_cascade(label="file")
menu_file=tk.Menu(menu_bar)
menu_file.add_command(Label="New Game")
menu_file.add_command(Label="Resume")
menu_file.add_command(Label="Salve")
menu_file.add_command(Label="Exit")

window.config(Menu=menu_bar)

#function of the botton
#def button1_function():
#    button_text=tk.Label(window,text="the button work well").pack()

#add botton
#button1=tk.Button(window,text="unuseful",command=button1_function).pack()

#C1=tk.Canvas

#start the main loop
window.mainloop()