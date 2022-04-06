A, B, C = input().split()
pi = 3.14159

A = float(A)
B = float(B)
C = float(C)

#A 
areatriangulo = (A * C) / 2
#B
areacirculo = pi * C**2
#C
areatrapezio = (A + B) * C / 2
#D
areaquadrado = B**2
#E
arearetangulo = A * B



print("TRIANGULO: %.3f" % areatriangulo)
print("CIRCULO: %.3f" % areacirculo)
print("TRAPEZIO: %.3f" % areatrapezio)
print("QUADRADO: %.3f" % areaquadrado)
print("RETANGULO: %.3f" % arearetangulo)