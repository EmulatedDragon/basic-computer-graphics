from cmath import pi
from turtle import circle
from graphics import *
import numpy as np
# functions


def pointf():
    t = """
    keep on giving points x and y 
    and to stop inputting press s
    ex: 12 2 4 5 s would be 
    (12,2) and (4,5)
    """
    output = Text(Point(900, 350), t)
    output.draw(win)
    s = ""
    temp = ""
    while True:
        temp = win.getKey()
        if temp == "s":
            break
        s += temp
    l = s.split("space")
    print(l)
    for i in range(len(l)//2):
        temp = Point(((int(l[2*i])))*20+400, -((int(l[2*i+1])))*20+400)
        circleasd = Circle(temp, 5)
        circleasd.draw(win)
    output.undraw()


def multilinef():
    t = """
    keep on giving points x and y 
    and to stop inputting press s
    ex: 12 2 4 5 s would be 
    (12,2) and (4,5)
    """
    output = Text(Point(900, 350), t)
    output.draw(win)
    s = ""
    temp = ""
    while True:
        temp = win.getKey()
        if temp == "s":
            break
        s += temp
    l = s.split("space")
    print(l)
    for i in range(len(l)//2):
        temp = Point(((int(l[2*i])))*20+400, -((int(l[2*i+1])))*20+400)
        circleasd = Circle(temp, 5)
        circleasd.draw(win)
    for i in range(len(l)//4):
        lineasd = Line(Point(((int(l[2*i])))*20+400, -((int(l[2*i+1])))*20+400),
                       Point(((int(l[2*i+2])))*20+400, -((int(l[2*i+3])))*20+400))
        lineasd.setWidth(2)
        lineasd.draw(win)
    output.undraw()


def circlef():
    t = """
    give points x and y and r
    and to stop inputting press s
    ex: 12 2 4 s would be 
    x=12 y=2 and r=4
    """
    output = Text(Point(900, 350), t)
    output.draw(win)
    s = ""
    temp = ""
    while True:
        temp = win.getKey()
        if temp == "s":
            break
        s += temp
    l = s.split("space")
    print(l)
    circleasd = Circle(
        Point((int(l[0]))*20+400, -(int(l[1]))*20+400), int(l[2])*20)
    circleasd.draw(win)
    output.undraw()


# graph creation
win = GraphWin("graph", 1000, 800)
# win.setBackground("black")
s = """give command in 
command box(case sensitive)
---------------
point - p
circle - c
multiline tool - l
transformations:
rotate about  - R
translate - T
scale - S
exit - e
-------------
if more than 1 value
have to be space seperated
"""
instructions = Text(Point(900, 150), s)
instructions.draw(win)
inputbox = Entry(Point(900, 300), 5)
inputbox.draw(win)

# draw axis
x_axis = Line(Point(400, 0), Point(400, 800))
y_axis = Line(Point(0, 400), Point(800, 400))
x_axis.setWidth(3)
y_axis.setWidth(3)
x_axis.setOutline("blue")
y_axis.setOutline("blue")
x_axis.draw(win)
y_axis.draw(win)
# draw grid
for i in range(0, 800, 20):
    tempx = Line(Point(i, 0), Point(i, 800))
    tempy = Line(Point(0, i), Point(800, i))
    tempx.setWidth(1)
    tempy.setWidth(1)
    tempx.setOutline("blue")
    tempy.setOutline("blue")
    tempx.draw(win)
    tempy.draw(win)
# input take
while(True):
    inp = win.getKey()
    if inp == 'e':
        break
    elif inp == 'p':
        pointf()
    elif inp == 'c':
        circlef()
    elif inp == 'l':
        multilinef()
    else:
        print("works")
print(inp)
win.getMouse()
win.close()
