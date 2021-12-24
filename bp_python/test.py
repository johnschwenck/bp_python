import pandas as pd

def test_fun(x):
    x += 1
    return(x)

def test_fun2(y):
    z = test_fun(y)
    return(z)
