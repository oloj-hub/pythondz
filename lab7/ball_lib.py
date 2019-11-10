class ball():
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if -self.vy<=self.gravity and -self.y+self.r >=585:
            self.gravity=0
            self.vy=0
        self.vy-=self.gravity
        if (self.x+self.vx+self.r>=800):
            self.vx=-self.vx/self.k
        if (self.x+self.vx-self.r<=0):
            self.vx=-self.vx/self.k
        if (self.y-self.vy+self.r>=585):
            self.vy=-self.vy/self.k
            self.vx=self.vx/self.k
        if (self.y-self.vy-self.r<=0):
            self.vy=-self.vy/self.k
        self.x += self.vx
        self.y -= self.vy
        self.canv.move(self.id,self.vx,-self.vy)

