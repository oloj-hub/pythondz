#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    i=0
    while not i==5:
        move_right()
        if cell_is_filled():
            i=i+1


if __name__ == '__main__':
    run_tasks()
