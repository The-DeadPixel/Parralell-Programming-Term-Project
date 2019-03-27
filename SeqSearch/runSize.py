import subprocess as sp
import sys

args = ['./SearchSeq', 'Exceptions.txt', 'SizeDocs/First', 'SizeDocs/Second', 'SizeDocs/Third']

seper = 'SearchSeq'
num = 1

for i in range(1,24):
    print((seper + str(num)))
    num += 1
    temp = args.copy()
    temp[2] += str(i)
    temp[3] += str(i)
    temp[4] += str(i)
    print(temp)
    #sp.call(temp)
    print('\n')

