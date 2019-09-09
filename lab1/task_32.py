#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    count=0
    while not wall_is_on_the_right():
        if wall_is_above():
            fill_cell()
        move_right()
        if not wall_is_above() and wall_is_beneath():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    count=count+1
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
    mov("ax",count)
if __name__ == '__main__':
    run_tasks()
