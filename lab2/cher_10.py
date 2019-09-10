import turtle as tu
import math
tu.color("pink")
def okr(r):
    for i in range(100):
        tu.forward(2*math.pi*r/100)
        tu.left(360/100)
r=50
tu.speed(10)
for i in range(3):
    okr(r)
    tu.left(180)
    okr(r)
    tu.left(240)
