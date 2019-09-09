#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    count=0
    i=0;
    while not wall_is_on_the_right():
        move_right()
        if i==count and not wall_is_on_the_right():
            i=0
            count+=1
            fill_cell()
        i=i+1
if __name__ == '__main__':
    run_tasks()
