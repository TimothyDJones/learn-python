# python_turtle.py
# Some examples of graphics drawing using Python Turtle graphics.
# https://www.pforprograms.com/2020/09/turtle-python-tutorials.html?m=1

import turtle

def display_screen(bg_color = "black"):
    wn = turtle.Screen()
    wn.bgcolor(bg_color)

def ninja_twist():
    display_screen()
    ninja = turtle.Turtle()
    ninja.speed(10)
    for i in range(180):
        ninja.forward(100)
        
