import ball
import tkinter
from random import randrange as rnd, choice

class bullet(ball.ball):
    def __init__(self,canv,bullets, x=40, y=450,r = 15):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.canv = canv
        self.bullets=bullets
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

