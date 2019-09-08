#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while not cell_is_filled():
        move_up()
    fill_cell()
    move_right()
    if cell_is_filled():
        fill_cell()
    else:
        move_left(n=2)
        fill_cell()
if __name__ == '__main__':
    run_tasks()
