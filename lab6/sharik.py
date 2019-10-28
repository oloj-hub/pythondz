from tkinter import *
from random import randrange as rnd, choice
import numpy as np
import time
import math 
class shar:
    def __init__(self, ball, txt, x, y,rad, per):
        self.ball = ball
        self.txt = txt
        self.x=x
        self.y=y
        self.rad=rad
        self.per=per
count=0
texts=[]
root = Tk()
a=800
b=600
root.geometry('800x600')
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
colors = ['red','orange','yellow','green','blue']
global balls
balls=[]

def rand_ball():
    global balls,i
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    sharik = shar(1,2,3,4,5,[6,7])
    sharik.x=x
    sharik.y=y
    col=choice(colors)
    sharik.rad=r
    sharik.per=np.array([x/500,y/500])
    sharik.ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = col)
    sharik.txt=canv.create_text(x,y,text=count,font="Times 25")
    balls.append(sharik)


def stolknovenie():
    for sharik in balls:
        if sharik.x+sharik.rad >= a or sharik.x-sharik.rad<=0:
            sharik.per[0]*=-1
        if sharik.y+sharik.rad>= b or sharik.y-sharik.rad<=0:
            sharik.per[1]*=-1
    for i in range(0,len(balls)-1):
        for j in range(i+1,len(balls)):
            sharik=balls[i]
            sharik1=balls[j]
            if ((sharik1.x-sharik.x)**2+(sharik1.y-sharik.y)**2)<=(sharik.rad+sharik1.rad)**2:
                n=np.array([sharik1.x-sharik.x,sharik1.y-sharik.y])
                n=n/np.linalg.norm(n)
                delta=np.dot(sharik.per,n)
                delta1=np.dot(sharik1.per,n)
                sharik.per-=delta*n
                sharik1.per-=delta1*n
                sharik.per+=delta1*n
                sharik1.per+=delta*n
            f=np.array([sharik1.x-sharik.x,sharik1.y-sharik.y])/((sharik1.x-sharik.x)**2+(sharik1.y-sharik.y)**2)**2
            sharik.per+=f
            sharik1.per-=f
                #delta=2*delta1*sharik1.rad**2/(sharik1.rad**2+sharik.rad**2)-delta*(sharik1.rad**2-sharik.rad**2)/(sharik1.rad**2+sharik.rad**2)
                #delta1=2*delta*sharik.rad**2/(sharik1.rad**2+sharik.rad**2)-delta1*(sharik.rad**2-sharik1.rad**2)/(sharik1.rad**2+sharik.rad**2)
    root.after(30,stolknovenie)
def move_balls():
    global count,balls,a,b
    for sharik in balls:
        if sharik.x+sharik.rad >= a or sharik.x-sharik.rad<=0:
            sharik.per[0]*=-1
        if sharik.y+sharik.rad>= b or sharik.y-sharik.rad<=0:
            sharik.per[1]*=-1
        canv.move(sharik.ball,sharik.per[0],sharik.per[1])
        canv.move(sharik.txt,sharik.per[0],sharik.per[1])
        sharik.x+=sharik.per[0]
        sharik.y+=sharik.per[1]
        #sharik.per[0]+=sharik.per[0]/10000
        #sharik.per[1]+=sharik.per[1]/10000
        canv.itemconfig(sharik.txt,text=count)
    root.after(10,move_balls)


def kill_ball(shar_id):
    c=0
    canv.delete(shar_id.ball)
    canv.delete(shar_id.txt)
    for sharik in balls:
        if sharik==shar_id:
            del balls[c]
        c+=1

def click(event):
    global count,balls
    for sharik in balls:
        if (event.x-sharik.x)**2+(event.y-sharik.y)**2 <= sharik.rad**2:
            count+=1
            kill_ball(sharik)
    rand_ball()

rand_ball()
move_balls()
stolknovenie()
canv.bind('<Button-1>',click)
mainloop()
