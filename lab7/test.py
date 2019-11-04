class ball():
    def set_coords(self):
        """возвращает квадрат описанный вокруг ballа"""
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        gravity=1
        self.vy-=gravity/2
        if (self.x+self.vx+self.r>=800):
            self.vx=-self.vx/2
        if (self.x+self.vx-self.r<=0):
            self.vx=-self.vx/2
        if (self.y-self.vy+self.r>=585):
            self.vy=-self.vy/2
            self.vx=self.vx/2
        if (self.y-self.vy-self.r<=0):
            self.vy=-self.vy/2
        self.vy-=gravity/2
        self.x += self.vx
        self.y -= self.vy
        self.canv.move(self.id,self.vx,-self.vy)

