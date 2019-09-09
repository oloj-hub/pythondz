#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while not wall_is_beneath():
        fill_cell()
        while not wall_is_on_the_right():
            move_right()
            fill_cell()
        while not wall_is_on_the_left():
            move_left()
        move_down()
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        fill_cell()
    while not wall_is_on_the_left():
        move_left()

if __name__ == '__main__':
    run_tasks()
