import turtle as tu
import math
tu.color("pink")
def prav_mnog(rad,n):
    fi=(n-2)/n*180#угол многоугольника
    tu.left(180-fi/2)#поворачиваем чтоб было под красивым углом
    for i in range(n):
        a=math.cos(math.pi*fi/180/2)*r*2 #длина стороны
        tu.forward(a)
        tu.left(180-fi)
    tu.right(180-fi+fi/2)
n=10
r0=20
r=20
for i in range(2,n,1):
    prav_mnog(r,i+1)
    r+=r0
    tu.penup()
    tu.forward(r-(i-1)*r0)
    tu.pendown()

