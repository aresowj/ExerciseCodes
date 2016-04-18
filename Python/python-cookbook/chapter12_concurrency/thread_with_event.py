# -*- coding: utf-8 -*-

import time
from threading import Thread, Event

# Code to execute in an independent thread
def count_down(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=count_down, args=(10, started_evt))
t.start()

# Wait for the thread to start
started_evt.wait()
print('countdown is running')

