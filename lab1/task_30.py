#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    c=0
    while not wall_is_on_the_right():
        move_right()
        c=c+1
    for i in range (c):
        for j in range (c):
            if i-j!=0 and c-i-j!=0:
                fill_cell()
            move_left()
        if i-c!=0 and i!=0:
            fill_cell()
        move_down()
        move_right(n=c)
    for j in range (c-1):
        move_left()
        fill_cell()
    move_left()
if __name__ == '__main__':
    run_tasks()
