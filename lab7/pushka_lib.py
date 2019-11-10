from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import ball_lib
import bullet_lib
import pushka_lib


class gun():
    def __init__(self,canv):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)
        self.canv = canv


    def fire2_start(self, event):
        """обьявляет начало выстрела"""
        self.f2_on = 1

    def fire2_end(self, event, vistrels, bullets):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_bullet = bullet_lib.bullet(self.canv)
        self.an = math.atan((event.y-new_bullet.y) / (event.x-new_bullet.x))
        new_bullet.vx = self.f2_power * math.cos(self.an)
        new_bullet.vy = - self.f2_power * math.sin(self.an)
        bullets += [new_bullet]
        self.f2_on = 0
        self.f2_power = 10
        vistrels[0] += 1


    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            self.canv.itemconfig(self.id, fill='orange')
        else:
            self.canv.itemconfig(self.id, fill='black')
        self.canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """ заставляет пушку удлиняться и менять цвет"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.canv.itemconfig(self.id, fill='orange')
        else:
            self.canv.itemconfig(self.id, fill='black')

