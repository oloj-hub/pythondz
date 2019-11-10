from random import randrange as rnd, choice
import tkinter as tk
import math
import time
# print (dir(math))
import ball_lib
import bullet_lib
import pushka_lib
import target_lib
import game_lib
class Game():
    def __init__(self,canv,*targets):
        self.bullets = []
        self.vistrels = []
        self.vistrels += [0]
        self.count_hits = 0
        self.targets = targets
        self.all_lives = 0
        self.screen1 = canv.create_text(200,200,text='')
        self.screen2 = canv.create_text(20,20,text='0')
        self.canv=canv
        self.z = 0.03


    def game_start(self):
        for target in self.targets:
            target.now_im_target()
            self.all_lives += target.live
        self.gun1 = pushka_lib.gun(self.canv)
        self.canv.bind('<Button-1>', self.gun1.fire2_start)
        self.canv.bind('<ButtonRelease-1>',lambda event: self.gun1.fire2_end(event,self.vistrels,self.bullets))
        self.canv.bind('<Motion>', self.gun1.targetting)
        self.canv.itemconfig(self.screen1, text='')


    def iterate(self):
        for target in self.targets:
            target.move()
        for bull in self.bullets:
            bull.move()
            bull.denay(self.bullets)
            for tar in self.targets:
                if bull.hittest(tar) and tar.live:
                    tar.live -= 1
                    self.count_hits = tar.hit(self.count_hits)
                    self.all_lives -= 1
        if self.all_lives == 0:
            self.canv.bind('<Button-1>', '')
            self.canv.bind('<ButtonRelease-1>', '')
            self.canv.itemconfig(self.screen1, text='Вы уничтожили цели за ' + str(self.vistrels[0]) + ' выстрелов')
        self.canv.itemconfig(self.screen2, text = str(self.count_hits))
        self.gun1.targetting()
        self.gun1.power_up()
        self.canv.update()
    def end_game(self):
        self.canv.itemconfig(self.screen1, text = '')
        self.vistrels[0] = 0
        self.canv.delete(self.gun1.id)


