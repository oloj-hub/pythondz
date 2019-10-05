from tkinter import *
import random
from time import sleep
import math
Width = 600
Height = 1000

main = Tk()

Window = Canvas(main, width=Width, height=Height, background="white")
Window.pack()

points=list()
global d
d=0
global q
q=0
def background():
	Window.create_rectangle(0, 0, Width, Height/2, fill="black")
	Window.create_rectangle(0, Height/2, Width, Height, fill="#851D32")
	Window.create_oval((300, 200), (540, 440), fill="#FFD000")
			
def rocket_launch():
	rocket()
	fire (120, 910, 140, 330, 260, 900, -1.6, -0.042, "yellow")
	fire (-35, 910, 75, 330, 100, 910, -0.05, -1.1, "yellow")
	fire (130, 908, 146, 450, 230, 902, -1.6, -0.05, "orange")
	fire (5, 910, 68, 460, 90, 909, -0.03, -1.2, "orange")
	fire (144, 906, 157, 660, 224, 904, -1.6, -0.05, "red")
	fire (15, 910, 58, 660, 74, 910, -0.03, -1.1, "red")

def rocket():
	Window.create_rectangle(130+rocket_S_x, 260+rocket_S_y, 85+rocket_S_x, 90+rocket_S_y, fill="grey", outline="#646464")
	Window.create_polygon((55+rocket_S_x, 290+rocket_S_y), (160+rocket_S_x, 290+rocket_S_y), (130+rocket_S_x, 260+rocket_S_y), (85+rocket_S_x, 260+rocket_S_y), fill="grey", outline="#646464")
	okno(95+rocket_S_x, 107.5+rocket_S_y, 12.5, 2, "#646464")
	okno(95+rocket_S_x, 145+rocket_S_y, 12.5, 2, "#646464")
	okno(95+rocket_S_x, 182.5+rocket_S_y, 12.5, 2, "#646464")
	Window.create_polygon((85+rocket_S_x, 90+rocket_S_y), (130+rocket_S_x, 90+rocket_S_y), (107.5+rocket_S_x, 55+rocket_S_y), fill="grey", outline="black")

def okno(x, y, r, w_window, color):
	Window.create_oval((x, y), (x+2*r, y+2*r), width=w_window, fill=color)

def fire(x1, y1, x2, y2, x3, y3, a1, a2, color):
	global points
	parabola(x1, y1, x2, y2, a1)
	parabola(x2, y2, x3, y3, a2)
	Window.create_polygon(points, fill=color, outline="black")
	points=[]

def parabola(x1, y1, x2, y2, a):
	x1=x1+rocket_S_x
	x2=x2+rocket_S_x
	y1=y1+rocket_S_y
	y2=y2+rocket_S_y
	b=((y1-y2)-(x1*x1-x2*x2)*a)/(x1-x2)
	c=y1-a*x1*x1-b*x1
	for x in range(x1, x2, 1):
		y=a*x*x+b*x+c
		points.append((x, y))

x0=400
y0=500

def astronaut(color, line_color):
	r_leg(color, line_color)
	l_leg(color, line_color)
	body(color, line_color)
	r_hand(color, line_color)
	l_hand(color, line_color)
	head(color, line_color)
	bullets()
	gun("blue")

def r_leg(color, line_color):
	global x0, y0
	Window.create_oval((x0+5, y0+23), (x0+35, y0+115), fill=color, outline=line_color)
	Window.create_oval((x0+35, y0+85), (x0+7, y0+135), fill=color, outline=line_color)
	Window.create_oval((x0+55, y0+115), (x0+7, y0+137), fill=color, outline=line_color)

def l_leg(color, line_color):
	global x0, y0
	Window.create_oval((x0-35, y0+23), (x0-5, y0+115), fill=color, outline=line_color)
	Window.create_oval((x0-35, y0+85), (x0-7, y0+135), fill=color, outline=line_color)
	Window.create_oval((x0-55, y0+115), (x0-7, y0+137), fill=color, outline=line_color)

def body(color, line_color):
	global x0, y0
	Window.create_oval((x0-35, y0-50), (x0+35, y0+50), fill=color, outline=line_color)	

def r_hand(color, line_color):
	global x0, y0
	Window.create_oval((x0+40, y0-34), (x0+65, y0-9), fill=color, outline=line_color)
	Window.create_oval((x0+53, y0-19), (x0+78, y0+6), fill=color, outline=line_color)
	Window.create_oval((x0+18, y0-50), (x0+48, y0-20), fill=color, outline=line_color)

def l_hand(color, line_color):
	global x0, y0
	Window.create_oval((x0-45, y0-40), (x0-70, y0-15), fill=color, outline=line_color)
	Window.create_oval((x0-65, y0-38), (x0-90, y0-13), fill=color, outline=line_color)
	Window.create_oval((x0-20, y0-46), (x0-50, y0-16), fill=color, outline=line_color)

def head(color, line_color):
	global x0, y0
	Window.create_oval((x0-25, y0-81), (x0+25, y0-40), fill=color, outline=line_color)
	Window.create_oval((x0-22, y0-76), (x0+20, y0-46), fill="black", outline=line_color)

def gun(color):
	global x0, y0
	Window.create_line((x0-77.5, y0-25.5), (x0-82.5, y0-42.5), width=10, fill=color)
	Window.create_line((x0-75.5, y0-42.5), (x0-117.5, y0-42.5), width=10, fill=color)

bullet_x0=x0
bullet_y0=y0
bullet_v_x=-3
bullet_v_y=0
bullet_ident=0
bullet_list=list()
bullet_list_x=list()
bullet_list_y=list()

def shoot(pressed_button):
	global bullet_ident
	x = Window.create_line((bullet_x0-117.5, bullet_y0-42.5), (bullet_x0-107.5, bullet_y0-42.5), width=5, fill="green")
	bullet_list.append(x)
	bullet_list_x.append(bullet_x0-117.5)
	bullet_list_x.append(bullet_x0-107.5)
	bullet_list_y.append(bullet_y0-42.5)
	bullet_ident += 1
	gun("blue")

def bullets():
	global x0, y0, bullet_x0, bullet_y0, bullet_ident
	bullet_x0=x0
	bullet_y0=y0
	for i in range(0, bullet_ident):
		bullet_list_x[2*(i-1)] += bullet_v_x
		bullet_list_x[2*(i-1)+1] += bullet_v_x
		bullet_list_y[i-1] += bullet_v_y
		x = Window.create_line((bullet_list_x[2*(i-1)], bullet_list_y[i-1]), (bullet_list_x[2*(i-1)+1], bullet_list_y[i-1]), width=5, fill="green")
		bullet_list[i-1] = x
	
astronaut_x_V=1
astronaut_y_V=2

def control(pressed_button):
	global astronaut_x_V, astronaut_y_V, x0, y0
	if pressed_button.keysym == "Up":
		y0 += -astronaut_x_V
	elif pressed_button.keysym == "Down":
		y0 += astronaut_y_V
	elif pressed_button.keysym == "Right":
        	x0 += astronaut_y_V
	elif pressed_button.keysym == "Left":
        	x0 += -astronaut_y_V

rocket_S_x=0
rocket_S_y=300
rocket_V_x=0
rocket_V_y=0
sleep_identif=0

def process():
        global rocket_S_y, rocket_S_x, rocket_V_y, rocket_V_x, bullet_ident,d,q
        Window.delete("all")
        background()
        if d<=500:
            rocket_launch()
            rocket_S_y += rocket_V_y
            rocket_S_x += rocket_V_x
            rocket_V_y += -0.01
            d+=1
        elif q<=210:
            rocket()
            rocket_S_y -= rocket_V_y
            rocket_S_x -= rocket_V_x
            rocket_V_y += -0.01
            q+=1
        Window.create_rectangle(0, 3*Height/5, Width, Height, fill="#851D32", outline="#851D32")
        astronaut("grey", "black")
        if q==211:
            for i in range (10,(d-490)*10,10):
                Window.create_oval((math.fabs(130+rocket_S_x+d/3-30-i),math.fabs( 290-i+rocket_S_y+d/3-30)), (math.fabs(85+rocket_S_x-d/3-30+i),math.fabs( 190+rocket_S_y+i-d/3-30)), fill='red')
            d+=1
        main.after(10, process)
Window.focus_set()
Window.bind("<space>", shoot)
Window.bind("<KeyPress>", control)

process()
main.mainloop()
