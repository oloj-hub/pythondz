#!/usr/bin/python3

from pyrob.api import *

@task
def task_2_1():
    move_right(n=2)
    move_down(n=2)
    krest()
    move_left()
    move_up()
def krest():
    fill_cell()
    move_down()
    fill_cell()
    move_up(n=2)
    fill_cell()
    move_down()
    move_right()
    fill_cell()
    move_left(n=2)
    fill_cell()
    move_right()

if __name__ == '__main__':
    run_tasks()
