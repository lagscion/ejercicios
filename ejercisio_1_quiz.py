# INSTRUCCIONES
# Resuelva las siguientes situaciones con algoritmos en Python
# 1. Se coloca un capital C, a un interés I (que oscila entre 0 y 100), durante M años y se desea
# saber en cuanto se habrá convertido ese capital en “M” años, sabiendo que es acumulativo.
# (Desarrollarlo con un algoritmo iterativo –for, while, etc-).






while  True :
    try:
        capital = int(input("ingrese su capital: "))

        interes = int(input("ingrese la tasa de su interes entre 0 y 100: "))

        años = int (input("en cuantos años piensas pagarlo: "))

        if  0 <= interes  <= 100 and 0 < capital and 0 < años:
            break

        else:
            print("el valor ingresado no es valido")

    except ValueError:
        print("el valor ingresado no es valido")





