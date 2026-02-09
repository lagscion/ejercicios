from tkinter import PROJECTING
from cupshelpers import Printer


campers = ["Andres", "Julian", "Alberth"]

print(campers)

# LEN()
print(len(campers))

# APPEND() : agrega al final
campers.append("Nicolle")
print(campers, len(campers))

# POP([indice]) : Elimina y devuelve el elemento indicado (por defecto es el último)
elem = campers.pop(1)
print(elem, campers, len(campers))

# EXTEND: añade todos los elementos de otra lista
grupo = ["Sebastian", "Samuel", "Jaime"]
# campers.append(grupo)
campers.extend(grupo)
print(campers, len(campers))

# INDEX(): devuelve la posición de la primera ocurrencia
try:
    pos = campers.index("Sebastian")
    print(pos)
    pos = campers.index("Luz")
    print(pos)
except ValueError:
    print("No se encuentra en la lista")

# IN / NOT IN:
# Verifica (True o False) si un elemento esá en la lista
print("Sebastian" in campers)
print("Luz" not in campers)

# Remove(valor)
# Elimina la primera ocurrrencia del valor en la lista

campers.append("Luz")
campers.append("Daniel")
print(campers)
try:
    campers.remove("Luz")
    print(campers)
except ValueError:
    print("No se encuentra en la lista")

# sort
# Ordena lexicográficamente
campers.sort()
print(campers)
campers.sort(reverse=True)
print(campers)

# SLICING[ini:Fin]
print(campers[1::2])

# REVERSE(): Invierte
campers.reverse()  # campers[::-1]
print(campers)


# INSERT(pos, elem): inserta un elemento en una posición
campers.insert(0, "Junior")
print(campers)

# COUNT(): cuenta cuantas veces aparece un valor
print(campers.count("junior"))

# CLEAR(): Elimina todos los elementos
# campers.clear() # campers = [] o campers = list()

# SORTED(): ordena sin modificar la lista
campers_ord = sorted(campers)
print(campers)
print(campers_ord)

# MIN(): encuentra menor valor de la lista
menor = min(campers)
print(menor)

# MAX(): encuentra el mayor valor de la lista
mayor = max(campers)

# SUM(); suma los elementos numéricos de la lista

# + : concatena 2 lista
print([19, 28, 20, 22] + [17, 18, 20] + [16, 17, 19])

# * : repite la lista
primos = [False] * 10
print(primos)

# Recorrido de listas 

# 1. por indice
for c in range (len(campers)):
    print ( campers[c], end=", ")

#2. por contenido:
for camper in campers :
    print()