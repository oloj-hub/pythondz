#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    for i in range (13):
        move_down()
        for j in range (i+1):
            move_right()
            fill_cell()
        while not wall_is_on_the_left():
            move_left()
    move_down()
    move_right()



if __name__ == '__main__':
    run_tasks()
