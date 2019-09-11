import turtle as tu
import math
from time import sleep
tu.color("pink")
tu.speed(10)
def okr(r):
    for i in range(100):
        tu.forward(2*math.pi*r/100)
        tu.left(360/100)
def duga(r,fi):
    for i in range(100):
        a=math.pi*fi/180*r #dlina dugi
        tu.forward(a/100)
        tu.right(fi/100)
def lico(r):
    tu.pendown()
    tu.begin_fill()
    okr(r)
    tu.color('yellow')
    tu.end_fill()
    tu.color('pink')
    tu.penup()
def glaz(r):
    tu.pendown()
    tu.begin_fill()
    okr(r)
    tu.color('blue')
    tu.end_fill()
    tu.color('pink')
    tu.penup()
def smile(r):
    tu.pendown()
    tu.width(3)
    tu.color('red')
    duga(r,180)
    tu.color('pink')
    tu.penup()
    tu.width(1)
def nose(r):
    tu.pendown()
    tu.width(3)
    tu.color('black')
    tu.forward(r)
    tu.color('pink')
    tu.penup()
    tu.width(1)
def oba_glaza(r,d):
    tu.left(90)
    tu.forward(d/2)
    glaz(r)
    tu.left(180)
    tu.forward(d)
    tu.right(90)
    tu.forward(2*r)
    tu.left(90)
    glaz(r)

def risunok(k):
    lico(k*100)
    tu.left(90)
    tu.forward(k*100)
    nose(20*k)
    tu.forward(k*40)
    oba_glaza(k*10,k*100)
    tu.right(90)
    tu.forward(20*k)
    smile(50*k)
risunok(2)
sleep(10)
