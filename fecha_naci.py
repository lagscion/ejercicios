#pergunta a el usuario
from curses.ascii import isdigit


fecha = input ("ingrese su fecha de nacimiento (dd/mm/aaaa)")

fechas = fecha.split("/")


if len(fechas[0]) == 2 and len(fechas[1]) == 2 and len(fechas[2]) == 4 and fechas [0].isdigit and [1].isdigit() and fechas[2].isdigit:
        print ("\n","tu dia fue: ",fechas[0],"\n", "tu mes fue: ", fechas[1], "\n", "tu año fue: ", fechas[2])
else:
        print("formato invalido")


