from random import randrange as rnd, choice
import tkinter as tk
import math
import time
# print (dir(math))
import ball
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

class bullet(ball.ball):
    def __init__(self,canv,bullets,gravity=1,x=40, y=450,r = 15,k=2):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.canv = canv
        self.bullets=bullets
        self.gravity=gravity
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30
        self.timer = 100
        self.k=k


    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x-obj.x)**2+(self.y-obj.y)**2<=(obj.r+self.r + 1)**2:
            return True
        else:
            return False


    def denay(self):
        """ уничтожает потрон через timer фрэймов"""
        self.timer-=1
        if (self.timer==0):
            self.bullets.remove(self)
            self.canv.delete(self.id)


class gun():
    def __init__(self,canv):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)
        self.canv=canv
    def fire2_start(self, event):
        """обьявляет начало выстрела"""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global bullets,vistrels
        new_bullet = bullet(self.canv,bullets)
        self.an = math.atan((event.y-new_bullet.y) / (event.x-new_bullet.x))
        new_bullet.vx = self.f2_power * math.cos(self.an)
        new_bullet.vy = - self.f2_power * math.sin(self.an)
        bullets += [new_bullet]
        self.f2_on = 0
        self.f2_power = 10
        vistrels+=1

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """ заставляет пушку удлиняться и менять цвет"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target(ball.ball):
    def __init__(self,canv,gravity=0.2,k=1):
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.canv = canv
        self.vx=rnd(-5,5)
        self.vy=rnd(-5,5)
        self.gravity=gravity
        self.k=k

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 760)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        self.canv.coords(self.id, x-r, y-r, x+r, y+r)
        self.canv.itemconfig(self.id, fill=color)

    def hit(self, screen):
        """Попадание шарика в цель."""
        global count
        self.canv.coords(self.id, -10, -10, -10, -10)
        self.canv.itemconfig(screen,text=int(count))
        count+=1


def on_closing():
    lines=''
    with open('top_results.txt','r') as f:
        govnocode=f.readlines()
        i=0
        if (len(govnocode)==0):
            govnocode.append(str(t1.points))
        else:
            while len(govnocode)>i and int(govnocode[i][0])>=t1.points:
                i+=1
            govnocode.insert(i,str(t1.points)+'\n')
        for line in govnocode:
            lines+=line
        f.close()
    with open('top_results.txt','w') as f:
        f.write(lines)
        f.close()
    root.destroy()

bullets=[]
count=0
vistrels=0
screen2=canv.create_text(20,20,text='0')


def new_game(event=''):
    global bullets,bullet,visterls,t1,t2
    screen1 = canv.create_text(400, 300, text='', font='28')
    t1 = target(canv)
    t2 = target(canv)
    g1 = gun(canv)
    t1.new_target()
    t2.new_target()
    bullets = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    canv.itemconfig(screen1, text='')
    z = 0.03
    t1.live = 1 
    t2.live = 1
    while t1.live or bullets or t2.live:
        for b in bullets:
            b.move()
            b.denay()
            if b.hittest(t1) and t1.live:
                t1.live -= 1
                t1.hit(screen2)
            if b.hittest(t2) and t2.live:
                t2.live-=1
                t2.hit(screen2)
            if t1.live==0 and t2.live==0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(vistrels) + ' выстрелов')
        t1.move()
        t2.move()
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(g1.id)
    root.after(750, new_game)   

new_game()
root.mainloop()
