a = int(input("ingrese primer numero"))
b = int(input("ingrese segundo numero"))
if a == b:
    print("los numeros son iguales")
elif a > b:                     #!elif me sirve para usar el if/else dentro de un if
        print("el primer numero es mayor")
else: 
        print("el segundo numero es mayor")