string = open('string.py', 'r')

line = string.read()

while line:
    values = line.split()
    line = string.read()

string.close()



