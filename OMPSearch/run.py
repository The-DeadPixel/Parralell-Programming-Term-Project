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
threads = 'export OMP_NUM_THREADS='
for t in range(2,9):
    print(threads + str(t))
    sp.Popen(threads + str(t), shell=True)
    for i in range(2,10):
        #print((seper + str(num)))
        print(args)
        # file output order
        #stem = 0.0 #stem
        #lexo = 0.0 #lexo
        #calc = 0.0 #calc
        #tot = 0.0 #total
        #flop = 0.0 #flops
        #byte = 0.0 #byte
        #for s in range(0,2):
            #value = sp.check_output(''.join(args),shell=True)
            #value = value.decode().split()
            #stem += float(value[0])
            #lexo += float(value[1])
            #calc += float(value[2])
            #tot += float(value[3])
            #flop += float(value[4])
            #byte += float(value[5])
        #stem = stem/2
        #lexo = lexo/2
        #calc = calc/2
        #tot = tot/2
        #flop = flop/2
        #byte = byte/2
        #print(stem, '\n', lexo, '\n', calc, '\n', tot, '\n', flop, '\n', byte, '\n')
        temp = Doc + str(num + i) + ' '
        args.append(temp)
        num += 3
    
#args1 = [' ./searchOMP', ' Exceptions.txt', ' First', ' Second', ' Third']

#seper1 = 'searchOMP'
#num1 = 1
#for t in range(1,9):
    #print(threads + str(t))
    #sp.Popen(threads + str(t), shell=True)
    #for f in range(1,24):
        ##print((seper1 + str(num1)))
        #num1 += 1
        #temp = args1.copy()
        #temp[2] += str(f)
        #temp[3] += str(f)
        #temp[4] += str(f)
        ##print(temp)
        ## file output order
        #stem = 0.0 #stem
        #lexo = 0.0 #lexo
        #calc = 0.0 #calc
        #tot = 0.0 #total
        #flop = 0.0 #flops
        #for i in range(0,4):
            #value = sp.check_output(''.join(temp),shell=True)
            #value = value.decode().split()
            ##print(value)
            #stem += float(value[0])
            #lexo += float(value[1])
            #calc += float(value[2])
            #tot += float(value[3])
            #flop += float(value[4])
        #stem = stem/4
        #lexo = lexo/4
        #calc = calc/4
        #tot = tot/4
        #flop = flop/4
        #print(stem, '\n', lexo, '\n', calc, '\n', tot, '\n', flop, '\n')
