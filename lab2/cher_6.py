import turtle as tu
tu.color('pink')
n=12
x=20
for i in range(n):
    tu.forward(x)
    tu.left(180)
    tu.forward(x)
    tu.left(180)
    tu.left(360/n)

