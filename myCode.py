import re
def read1_function():
    f = open('text.txt', 'r')
    j = f.read()
    f.close()
    arr = list()
    arr = j.split('\n')
    print(arr)
    return(arr)

def read2_function():
    f = open('text2.txt', 'r')
    j = f.read()
    f.close()
    arr = list()
    arr = j.split('\n')
    print(arr)
    return(arr)