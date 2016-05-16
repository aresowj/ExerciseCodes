# -*- coding: utf-8 -*-

import threading
import time

class SharedCounter:
    """A counter object that can be shared by multiple threads."""
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        """Increment the counter with locking"""
        with self._value_lock:
            self._value += delta
            print(self._value)
            time.sleep(5)

    def decr(self, delta=1):
        """Decrement the counter with locking"""
        with self._value_lock:
            self._value -= delta
            print(self._value)

counter = SharedCounter(10)
t1 = threading.Thread(target=counter.incr)
t2 = threading.Thread(target=counter.decr)
t1.start()
t2.start()
