from __future__ import absolute_import
from proj.celery import app

@app.task
def split():
    task_count = 10
    return task_count

@app.task
def run(task_count):
    for i in range(task_count):
        subtask.delay(i)

# このへんに新しいrunを作る。
# SQSは遅すぎて話にならないのでRDSにキューイング用のテーブルを作って動かしてみよう！


@app.task
def subtask(index):
    print("Processing " + str(index))
