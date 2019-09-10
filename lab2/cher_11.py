import turtle as tu
import math
tu.color("pink")
def okr(r):
    for i in range(100):
        tu.forward(2*math.pi*r/100)
        tu.left(360/100)
r0=50
r=30
tu.speed(10)
n=10
tu.right(90)
for i in range(n):
    okr(r0)
    tu.left(180)
    okr(r0)
    tu.left(180)
    r0+=r

