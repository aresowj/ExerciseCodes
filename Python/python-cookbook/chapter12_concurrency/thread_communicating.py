# -*- coding: utf-8 -*-

import random
import time
from queue import Queue
from threading import Thread


def producer(out_q):
    """A thread that produces data"""
    while True:
        # Produce some data
        time.sleep(2)
        out_q.put(random.random())


def consumer(in_q):
    """A thread that consumes data"""
    while True:
        # Get some data
        time.sleep(2)
        data = in_q.get()
        print(data)

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
