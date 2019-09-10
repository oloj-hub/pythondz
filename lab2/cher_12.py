import turtle as tu
import math
tu.color("pink")
def duga(r,fi):
    for i in range(100):
        a=math.pi*fi/180*r #dlina dugi
        tu.forward(a/100)
        tu.right(fi/100)
r0=50
r1=10
tu.speed(10)
n=5
tu.left(90)
for i in range(n):
    duga(r0,180)
    duga(r1,180)

