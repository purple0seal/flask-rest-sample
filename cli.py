import os
import json
from lib.validator import calculate

def readFile(filename):
    f = open(filename)
    data = f.read()
    f.close()
    return data

fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = "resources/input.json"


params = readFile(filename)
dict = json.loads(params)

print calculate(dict['a'], dict['b'])
