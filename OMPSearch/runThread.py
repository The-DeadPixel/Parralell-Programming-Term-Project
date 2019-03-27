import subprocess as sp
import sys

args = ['./searchOMP ', 'Exceptions.txt ', 'Doc1 ', 'Doc2 ', 'Doc3 ']

#var = 'Doc'
#num = 1
#var = var + str(num)
#print(var)

Doc = 'Doc'
seper = 'searchOmp'
num = 3
#threads = 'export OMP_NUM_THREADS=2'
#sp.Popen(threads, shell=True)
    
for i in range(2,10):
    #print((seper + str(num)))
    #print(args)
    # file output order
    stem = 0.0 #stem
    lexo = 0.0 #lexo
    calc = 0.0 #calc
    tot = 0.0 #total
    flop = 0.0 #flops
    byte = 0.0 #byte
    for s in range(0,4):
        value = sp.check_output(''.join(args),shell=True)
        value = value.decode().split()
        stem += float(value[0])
        lexo += float(value[1])
        calc += float(value[2])
        tot += float(value[3])
        flop += float(value[4])
        byte += float(value[5])
    stem = stem/4
    lexo = lexo/4
    calc = calc/4
    tot = tot/4
    flop = flop/4
    byte = byte/4
    print(stem, '\n', lexo, '\n', calc, '\n', tot, '\n', flop, '\n', byte, '\n')
    temp = Doc + str(num + i) + ' '
    args.append(temp)
    num += 3
