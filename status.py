from .grades import Avg

def status(grades):
    if Avg(grades) > 10:
        return "Acc"
    else:
        return "Fail"