# -*- coding: utf-8 -*-

# Code to execute in an independent thread
import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# Create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,), daemon=True)
t.start()

while t.is_alive():
    print('Still running...')
    time.sleep(2)

print('Completed.')

