from PIL import Image
from graph import *
import numpy as np
import math

global ls
ls = [[0, 0], [0, 0], [0, 0]]
global i
i = 0
global obj
obj = point(0, 0)
global fn1
global fn2
global col
global pol
global res
global kost
res = open('rez.py', 'w')
res.write("from graph import *\n")
res.write("import math\n")
res.write("windowSize(2000, 1000)\n")
res.write("canvasSize(2000, 1000)\n")
pol = []
col = 'white'
res.write("def elips(x1,y1,x2,y2):\n")
res.write("    a=(x2-x1)/2\n")
res.write("    b=(y2-y1)/2\n")
res.write("    kost=[]\n")
res.write("    for fi in range(1,360,1):\n")
res.write("        y=int(b*math.sin(fi*math.pi/180)+y1+b)\n")
res.write("        x=int(a*math.cos(fi*math.pi/180)+x1+a)\n")
res.write("        kost.append((x,y))\n")
res.write("    obj=polygon(kost)\n")


def mouseClickLine(event):
    global i
    global ls
    global obj
    if obj != 0:
        deleteObject(obj)
        obj = point(0, 0)
    x = event.x
    y = event.y
    ls[i][0] = x
    ls[i][1] = y
    i += 1
    point(x, y)
    if i == 2:
        pol.append([ls[0][0], ls[0][1]])
        pol.append([ls[1][0], ls[1][1]])
        line(ls[0][0], ls[0][1], ls[1][0], ls[1][1])
        ls = [[0, 0], [0, 0], [0, 0]]
        i = 0


def mouseClickElips(event):
    global i
    global ls
    global objel
    global kost
    x = event.x
    y = event.y
    ls[i][0] = x
    ls[i][1] = y
    i += 1
    point(x, y)
    if i == 2:
        elips(ls[0][0], ls[0][1], ls[1][0], ls[1][1])
        obj = point(0, 0)
        i = 0
        res.write("brushColor(")
        res.write("'")
        res.write(col)
        res.write("'")
        res.write(")\n")
        # res.write("polygon(")
        # res.write(str:q(kost))
        # res.write(")\n")
        res.write('elips(')
        res.write(str(ls[0][0]))
        res.write(',')
        res.write(str(ls[0][1]))
        res.write(',')
        res.write(str(ls[1][0]))
        res.write(',')
        res.write(str(ls[1][1]))
        res.write(')\n')
        ls = [[0, 0], [0, 0], [0, 0]]


def MouseMoveLine(event):
    global i
    global ls
    global obj
    if i == 1:
        deleteObject(obj)
        x = event.x
        y = event.y
        obj = line(ls[0][0], ls[0][1], x, y)


def MouseMoveElips(event):
    global i
    global ls
    global obj
    if i == 1:
        deleteObject(obj)
        obj = point(0, 0)
        x = event.x
        y = event.y
        elips(ls[0][0], ls[0][1], x, y)


def elips(x1, y1, x2, y2):
    global obj
    global kost
    a = (x2 - x1) / 2
    b = (y2 - y1) / 2
    kost = []
    brushColor(col)
    for fi in range(1, 360, 1):
        y = int(b * math.sin(fi * math.pi / 180) + y1 + b)
        x = int(a * math.cos(fi * math.pi / 180) + x1 + a)
        kost.append((x, y))
    obj = polygon(kost)


def change():
    global fn1
    global fn2
    if fn1 == mouseClickLine:
        fn1 = mouseClickElips
        fn2 = MouseMoveElips
    else:
        fn1 = mouseClickLine
        fn2 = MouseMoveLine
    otmena(0)
    onMouseClick(fn1, 1)
    onMouseMove(fn2)


def changecolor():
    global col
    if col == 'white':
        col = 'yellow'
        button("yellow", 400, 15, width=30, command=changecolor)
    elif col == 'yellow':
        col = 'black'
        button("black", 400, 15, width=30, command=changecolor)
    elif col == 'black':
        col = 'gray'
        button("gray", 400, 15, width=30, command=changecolor)
    elif col == 'gray':
        col = 'red'
        button("red", 400, 15, width=30, command=changecolor)
    elif col == 'red':
        col = 'blue'
        button("blue", 400, 15, width=30, command=changecolor)
    elif col == 'blue':
        col = 'white'
        button("white", 400, 15, width=30, command=changecolor)


def otmena(event):
    global obj
    global i
    global ls
    deleteObject(obj)
    obj = point(0, 0)
    i = 0
    ls = [[0, 0], [0, 0], [0, 0]]


def poly():
    global pol
    global res
    otmena(0)
    brushColor(col)
    polygon(pol)
    res.write("brushColor(\'")
    res.write(str(col))
    res.write("\')\n")
    res.write("polygon(")
    res.write(str(pol))
    res.write(")\n")
    pol = []


def main():
    global ls
    global i
    global fn1
    global fn2
    fn2 = MouseMoveElips
    fn1 = mouseClickElips
    windowSize(2000, 1000)
    canvasSize(2000, 1000)
    onMouseClick(fn1, 1)
    onMouseMove(fn2)
    onMouseClick(otmena, 3)
    button("change", 100, 15, width=30, command=change)
    button("changecolor", 400, 15, width=30, command=changecolor)
    button("polygon", 700, 15, width=30, command=poly)
    run()


main()
res.write("run()")
res.close()
