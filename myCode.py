import re
def read1_function():
    f = open('text.txt', 'r')
    j = f.read()
    f.close()
    arr = list()
    arr = j.split('\n')
    return(arr)

def read2_function():
    f = open('text2.txt', 'r')
    j = f.read()
    f.close()
    arr = list()
    arr = j.split('\n')
    return(arr)

read1 = read1_function()
read2 = read2_function()