#!/usr/bin/env python2

import sys # usado para la funcion sys.exit 

target_int=raw_input("how many integrers?")

target_int=int(target_int)
except ValueError:
sys.exit("You must enter an integer")

ints=list()
count=0
while count < target_int:
new_int = raw_input("please enter integrer {0}:".format(count + 1))
isint=False
new_int=int(new_int)    
except:
print("you must enter an integer")
    
if isint ==True:
        #agrega el integer a la coleccion
        ints.append(new_int)
        #aumenta la cuenta +1
        count += 1
        
        print("using a for loop")
        for value in ints:
            print(str(value))
            
            #o con un loop while
            
print("using a while loop")
total = len(ints)
count= 0
while count < total:
        print(str(ints[count]))
        count += 1