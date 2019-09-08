#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while not wall_is_beneath():
        move_down()
    r=1
    l=1
    while not (l==0  and r==0):
        r=1
        while not wall_is_on_the_right() and wall_is_beneath():
            move_right()
        if not wall_is_beneath():
            while not wall_is_beneath():
                move_down()
        else:
            r=0
            while not wall_is_on_the_left() and wall_is_beneath():
                move_left()
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
            else: l=0;
if __name__ == '__main__':
    run_tasks()
