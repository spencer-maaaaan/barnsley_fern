"""
auth spencer tenney
desc generator of a sequence of points that plot a barnsley fern
"""
from random import choices

def Fern():
    # defining each transformation function
    f1 = lambda x,y: (0, 0.16*y)
    f2 = lambda x,y: (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
    f3 = lambda x,y: (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
    f4 = lambda x,y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)

    fs = [f1, f2, f3, f4]
    x,y = 0,0
    i = 0

    while True:
        # choosing a random function with numpy
        f = choices(fs, weights=(0.01,0.85,0.07,0.07))[0]

        # performing transformation and yielding
        x,y = f(x,y)
        yield x,y
