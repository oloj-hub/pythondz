import turtle as tu
from time import sleep
tu.color('pink')
def zvezda(n,d):
    a=180/n#углы звезды
    for i in range(n-1):
        tu.forward(d)
        tu.left(180-a)
    tu.forward(d)
tu.left(180)
zvezda(11,250)
sleep(5)    
