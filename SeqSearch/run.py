import subprocess as sp
import sys

args = ['./SearchSeq', 'Exceptions.txt', 'NumDocs/Doc1', 'NumDocs/Doc2', 'NumDocs/Doc3']

Doc = 'NumDocs/Doc'
seper = 'SearchSeq'
num = 3
for i in range(2,10):
    print((seper + str(num)))
    print(args)
    sp.call(args)
    for j in range(1,4):
        temp = Doc + str(num + j)
        args.append(temp)
    num += 3
    #print('\n')
    

#print('THIS IS ALL OF THE AVERAGE DATA FOR NUM LINE TEST')


#args1 = [' ./SearchSeq', ' Exceptions.txt', ' SizeDocs/First', ' SizeDocs/Second', ' SizeDocs/Third']

#seper1 = 'SearchSeq'
#num1 = 1

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
