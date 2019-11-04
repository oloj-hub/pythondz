from graph import *
import math
windowSize(2000, 1000)
canvasSize(2000, 1000)
def elips(x1,y1,x2,y2):
    a=(x2-x1)/2
    b=(y2-y1)/2
    kost=[]
    for fi in range(1,360,1):
        y=int(b*math.sin(fi*math.pi/180)+y1+b)
        x=int(a*math.cos(fi*math.pi/180)+x1+a)
        kost.append((x,y))
    obj=polygon(kost)
run()