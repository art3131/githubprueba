#!/usr/bin/env python2
import sys # usado para la funcion sys.exit
int_condition = 15 #condicion inicial =5
if int_condition < 6:
    sys.exit("int_condition must be >= 5")
else:
    print("int_condition was >= 6 - continuing")