from graph import *
import math
import numpy as np
windowSize(2000, 1000)
canvasSize(2000, 1000)
global xvostobj
global ptiza1
global ptiza2
global ptiza3
global rib
global i
global krilo1
global krilo2
def elips(x1,y1,x2,y2):
    a=(x2-x1)/2
    b=(y2-y1)/2
    kost=[]
    for fi in range(1,360,1):
        y=int(b*math.sin(fi*math.pi/180)+y1+b)
        x=int(a*math.cos(fi*math.pi/180)+x1+a)
        kost.append((x,y))
    obj=polygon(kost)
    return obj
def neboslices(pos,h0,l):
    c1=1
    c2=1
    c3=254
    delc=int(255/len(h0))
    for h in h0:
        brushColor(c1,c2,c3)
        c1+=delc
        c2+=int(delc/2)
        c3-=delc
        rectangle(pos[0],pos[1],pos[0]+l,pos[1]+h)
        pos[1]+=h
    brushColor(0,0,255)
    rectangle(pos[0],pos[1],pos[0]+l,1000)
def duga(x0,y0,r,fi0,fi1):
    penColor(0,0,0)
    penSize(3)
    kost=[]
    for i in range(fi0,fi1-1,1):
        y=-r*math.sin(i*math.pi/180)+y0
        x=-r*math.cos(i*math.pi/180)+x0
        x1=-r*math.cos((i+1)*math.pi/180)+x0
        y1=-r*math.sin((i+1)*math.pi/180)+y0
        kost.append(line(x,y,x1,y1))
    penSize(1)
    return kost
def bird(x,y,r,fi0,fi1):
    penColor("white")
    return [duga(x-r/2,y,r/2,fi0,fi1),duga(x+r/2,y,r/2,180-fi1,180-fi0)]
def telo():
    brushColor('white')
    return elips(319,677,526,761)
def sheya():
    brushColor('white')
    return elips(510,683,588,723)
def golova():
    brushColor('white')
    elips(570,662,630,702)
    brushColor("black")
    elips(608,669,615,676)
def klyuv():
    brushColor('yellow')
    polygon([[627, 677], [676, 671], [676, 671], [689, 679], [689, 679], [628, 683], [628, 683], [690, 680], [690, 680], [674, 697], [674, 697], [625, 688], [627, 677]])
def xvost():
    brushColor('white')
    polygon([[344, 693], [301, 650], [301, 650], [268, 698], [268, 698], [323, 720], [344, 693]])
def krilozad():
    brushColor('white')
    return polygon([[451, 683], [442, 593], [382, 572], [314, 528], [338, 590], [383, 622], [390, 672], [451, 683]])
def krilopered():
    brushColor('white')
    return polygon([[442, 687], [406, 615], [334, 602], [293, 579], [312, 625], [369, 639], [376, 683], [442, 687]])
def nogazad():
    brushColor('white')
    elips(420,749,455,809)
    brushColor('white')
    polygon([[450, 797], [488, 809], [489, 809], [512, 826], [511, 826], [504, 835], [504, 835], [450, 818], [450, 818], [438, 803], [450, 797]])
    brushColor('yellow')
    polygon([[511, 824], [548, 817], [546, 816], [523, 827], [523, 827], [543, 832], [543, 832], [517, 834], [517, 834], [532, 843], [530, 843], [511, 838], [511, 838], [508, 844], [508, 844], [503, 833], [511, 824]])
def nogapered():
    brushColor('white')
    elips(389,748,424,812)
    brushColor('white')
    polygon([[410, 806], [457, 829], [455, 829], [464, 846], [464, 846], [456, 854], [455, 854], [406, 823], [406, 822], [397, 803], [410, 806]])
    brushColor('yellow')
    polygon([[461, 847], [503, 855], [500, 854], [467, 855], [468, 856], [493, 868], [491, 868], [466, 862], [466, 863], [472, 880], [473, 879], [454, 854], [456, 858], [454, 865], [454, 865], [449, 850], [461, 847]])
def ptiza():
    global krilo1,krilo2
    nogazad()
    sheya()
    golova()
    klyuv()
    telo()
    xvost()
    krilo1=krilozad()
    krilo2=krilopered()
    nogapered()
def telo_rib():
    brushColor('gray')
    return elips(681,896,787,942)
def xvost_rib():
    brushColor('red')
    return polygon([[684, 915], [641, 894], [646, 931], [683, 923], [684, 915]])
def uppl_rib():
    brushColor('red')
    return polygon([[722, 902], [704, 880], [762, 879], [756, 901], [722, 902]])
def glaz_rib1():
    brushColor('blue')
    return elips(763,912,776,926)
def glaz_rib2():
    brushColor('black')
    return elips(771,921,770,922)
def glaz_rib3():
    brushColor('white')
    return elips(766,915,771,921)
def leftpl_rib():
    brushColor('red')
    return polygon([[703, 935], [693, 952], [693, 952], [714, 956], [714, 956], [720, 939], [703, 935]])
def rightpl_rib():
    brushColor('red')
    return polygon([[749, 940], [750, 956], [773, 947], [759, 933], [749, 940]])
def riba():
    global rib
    rib=[rightpl_rib(),
    leftpl_rib(),
    uppl_rib(),
    xvost_rib(),
    telo_rib(),
    glaz_rib1(),
    glaz_rib2(),
    glaz_rib3()
    ]
h=[100,50,100,200,200]
neboslices([0,0],h,1000)
ptiza1=bird(200,70,50,90,200)
ptiza2=bird(700,200,50,90,200)
ptiza3=bird(500,400,50,90,200)
riba()
ptiza()
i=-1
def update():
    global i
    global ptiza1,ptiza2,ptiza3
    global krilo1,krilo2
    for t in ptiza1[0]:
        deleteObject(t)
    for t in ptiza1[1]:
        deleteObject(t)
    ptiza1=bird(200+i*20,70+i*30,50,70+i*20,180+i*20)
    for t in ptiza2[0]:
        deleteObject(t)
    for t in ptiza2[1]:
        deleteObject(t)
    ptiza2=bird(700+i*20,200+i*30,50,70+i*20,180+i*20)
    for t in ptiza3[0]:
        deleteObject(t)
    for t in ptiza3[1]:
        deleteObject(t)
    ptiza3=bird(500+i*20,400+i*30,50,70+i*20,180+i*20)
    for t in rib:
        moveObjectBy(t,i*20,i*20)
    deleteObject(krilo1)
    if (i==1):
        brushColor("white")
        deleteObject(krilo1) 
        deleteObject(krilo2)
    else:
        brushColor("white")
        deleteObject(krilo1)
        krilo1=polygon([[451, 683], [442, 593], [382, 572], [314, 528], [338, 590], [383, 622], [390, 672], [451, 683]])
        deleteObject(krilo2)
        krilo2=polygon([[442, 687], [406, 615], [334, 602], [293, 579], [312, 625], [369, 639], [376, 683], [442, 687]])
    i=-i
onTimer(update,1000)
run()
