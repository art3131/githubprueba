a = True
b = False

print(a and a) # verdadero y verdadero = verdadero
print(a and b) # verdadero y falso = falso
print(b and b) # falso y falso = falso

print(a or a) # verdadero o verdadero = verdadero
print(a or b) # verdadero o falso = verdadero
print(b or a) # falso o verdadero = verdadero
print(b or b) # falso o falso = falso


print((3<4) and (4<5)) # T y T = T
print((4<3) and (4<5)) # F y T = T

#negacion -----> not
resultado = a and a #true and true
print(not resultado)
resultado = a and b #true and false
print(not resultado)