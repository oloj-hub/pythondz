from tkinter import *
from random import randrange as rnd, choice
import numpy as np
import time
import math


class shar:
    # шарики с g притягиваются к друг другу, per-перемещение за фрейм
    # счет летает с шариками (txt), это лучше чем выносить в отдельное окно
    def __init__(self, ball, txt, x, y, rad, per, gravity):
        self.ball = ball
        self.txt = txt
        self.x = x
        self.y = y
        self.rad = rad
        self.per = per
        self.g = gravity


count = 0
texts = []
root = Tk()
a = 800
b = 600
root.geometry('800x650')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
global balls
balls = []
n = 7


def rand_ball(n):
    # создание n шариков
    global balls
    for i in range(0, n):
        x = rnd(100, 700)
        y = rnd(100, 500)
        r = rnd(30, 50)
        k = rnd(200, 500)
        g = rnd(0, 1)
        sharik = shar(1, 2, 3, 4, 5, [6, 7], 8)
        sharik.x = x
        sharik.y = y
        col = choice(colors)
        sharik.rad = r
        sharik.per = np.array([x / k, y / k])
        sharik.gravity = g
        sharik.ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=col)
        sharik.txt = canv.create_text(x, y, text=count, font="Times 25")
        balls.append(sharik)


def stolknovenie():
    # обрабатывает удары об стену, шаров о друг друга и притяжение друг к другу
    for sharik in balls:
        if sharik.x + sharik.rad + sharik.per[0] >= a or sharik.x - sharik.rad + sharik.per[0] <= 0:
            sharik.per[0] *= -1
        if sharik.y + sharik.rad + sharik.per[1] >= b or sharik.y - sharik.rad + sharik.per[1] <= 0:
            sharik.per[1] *= -1
    for i in range(0, len(balls) - 1):
        for j in range(i + 1, len(balls)):
            sharik = balls[i]
            sharik1 = balls[j]
            if ((sharik1.x - sharik.x) ** 2 + (sharik1.y - sharik.y) ** 2) <= (sharik.rad + sharik1.rad) ** 2:
                n = np.array([sharik1.x - sharik.x, sharik1.y - sharik.y])
                n = n / np.linalg.norm(n)
                n *= (sharik1.rad + sharik.rad)
                canv.move(sharik1.ball, n[0] - (sharik1.x - sharik.x), n[1] - (sharik1.y - sharik.y))
                canv.move(sharik1.txt, n[0] - (sharik1.x - sharik.x), n[1] - (sharik1.y - sharik.y))
                sharik1.x += n[0] - (sharik1.x - sharik.x)
                sharik1.y += n[1] - (sharik1.y - sharik.y)
                n = n / np.linalg.norm(n)
                delta = np.dot(sharik.per, n)
                delta1 = np.dot(sharik1.per, n)
                sharik.per -= delta * n
                sharik1.per -= delta1 * n
                sharik.per += delta1 * n
                sharik1.per += delta * n
        if (sharik1.g and sharik.g):
            sharik1.per += np.array([sharik.x - sharik1.x, sharik.y - sharik1.y]) / 10000
            sharik.per += np.array([sharik1.x - sharik.x, sharik1.y - sharik.y]) / 10000


def move_balls():
    # двигает шарики и вызывает функцию их взаимодействия(stolknovenie)
    global count, balls, a, b
    stolknovenie()
    for sharik in balls:
        sharik.per += sharik.gravity
        canv.move(sharik.ball, sharik.per[0], sharik.per[1])
        canv.move(sharik.txt, sharik.per[0], sharik.per[1])
        sharik.x += sharik.per[0]
        sharik.y += sharik.per[1]
        canv.itemconfig(sharik.txt, text=count)
    root.after(10, move_balls)


def kill_ball(shar_id):
    # невероятно, но удаляет шарик по его id
    c = 0
    canv.delete(shar_id.ball)
    canv.delete(shar_id.txt)
    for sharik in balls:
        if sharik == shar_id:
            del balls[c]
        c += 1


def click(event):
    # проверка поподания по шарику и обработка попадания
    global count, balls
    for sharik in balls:
        if (event.x - sharik.x) ** 2 + (event.y - sharik.y) ** 2 <= sharik.rad ** 2:
            count += 1
            kill_ball(sharik)
            rand_ball(1)


def safe_result():
    # написанная ночью непонятно как работающие сохранение результатов в файл
    global count
    lines = ''
    with open('top_results.txt', 'r') as f:
        # считаю govnocode наиболее подходящим названием для переменной в данной ситуации
        govnocode = f.readlines()
        i = 0
        t = 0
        while len(govnocode) > t:
            if govnocode[t] == '\n':
                govnocode.remove('\n')
                t -= 1
            t += 1
        if (len(govnocode) == 0):
            govnocode.append(str(count))
        else:
            while len(govnocode) > i and int(govnocode[i][0]) >= count:
                i += 1
            govnocode.insert(i, str(count) + '\n')
        for line in govnocode:
            lines += line
        f.close()
    with open('top_results.txt', 'w') as f:
        f.write(lines)
        f.close()
    root.destroy()


# вызов всего что должно заставить игру работать, кнопка, позволяющая сохранить результат и ЗАКРЫВАЮЩАЯ ИГРУ
button = Button(root, text="safe result and exit", command=safe_result)
button.pack()
rand_ball(n)
move_balls()
canv.bind('<Button-1>', click)
mainloop()
