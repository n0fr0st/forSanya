import re
def read1_function():
    f = open('text.txt', 'r')
    j = f.read()
    f.close()
    arr = list()
    arr = re.split('\n.', j)
    return(arr)

def read2_function():
    f = open('text2.txt', 'r')
    j = f.read()
    f.close()
    arr = list()
    arr = re.split('. \n ',j)
    return(arr)