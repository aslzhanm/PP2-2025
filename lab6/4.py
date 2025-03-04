import time
import math

def delayed_sqrt(n, delay):
    time.sleep(delay / 1000)
    return math.sqrt(n)

print(delayed_sqrt(25100, 2123))
