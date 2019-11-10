from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import ball_lib
import bullet_lib
import pushka_lib

class target(ball_lib.ball):
    def __init__(self, canv, gravity=0.2,k=1,live=1):
        self.live = live
        self.id = canv.create_oval(0,0,0,0)
        self.canv = canv
        self.vx=rnd(-5,5)
        self.vy=rnd(-5,5)
        self.gravity=gravity
        self.k=k


    def now_im_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 760)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        self.canv.coords(self.id, x-r, y-r, x+r, y+r)
        self.canv.itemconfig(self.id, fill=color)
        self.live = 1


    def hit(self, count):
        """Попадание шарика в цель."""
        self.canv.coords(self.id, -10, -10, -10, -10)
        count+=1
        return count

