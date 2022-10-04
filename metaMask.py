from turtle import Turtle
from tkinter import *


def click():
    print('Works')


button = Button(text='Connect Meta Mask')
button.config(command=click)
button.pack()
