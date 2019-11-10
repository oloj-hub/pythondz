from random import randrange as rnd, choice
import tkinter as tk
import math
import time
# print (dir(math))
import ball_lib
import bullet_lib
import pushka_lib
import target_lib
import game_lib
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
target1 = target_lib.target(canv)
target2 = target_lib.target(canv)
game = game_lib.Game(canv,target1,target2)
def new_game():
    game.game_start()
    while game.all_lives or game.bullets:
        game.iterate()
        time.sleep(game.z)
    game.end_game()
    root.after(750, new_game)
new_game()
root.mainloop()
