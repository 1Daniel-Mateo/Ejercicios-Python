# creacion de un ciclo for, while, do while
# importacion de operaciones aritmeticas
import operator
import random


lista = []

# ciclo for

# for i in range(10):
#     n = random.randint(1, 100)
#     lista.append(n)

# print(lista)
    
# ciclo while

# ram = random.randrange(1,20)

# while ram > 1:
#     print("ciclo do-while", ram)
#     ram += 1
#     if ram >= 20:
#         break

# ciclo do-while
    
ingreso = input("escreibe s y te dira bienvenido")
    
while ingreso == "s":
    print("Bienvenido")
    ingreso = ("si quieres cerrar ciclo oprime n")

    if ingreso == "n":
        break

print("el ciclo se cerro")



