#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down()
    for i in range (4):
       krest()
       move_right(n=4)
    krest()
def krest():
    move_right()
    move_down()
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
    move_up()



if __name__ == '__main__':
    run_tasks()
