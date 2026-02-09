#+dd-dddd-dd



tel = input ("ingrese su numero: ")
partes_tel = tel.strip().split("-")

#validar formato

if len(partes_tel) == 3 and partes_tel [0][1:].isdigit() and partes_tel[1].isdigit() and partes_tel[2].isdigit== "+" and len(partes_tel[2]) == 2:
    print (partes_tel [1])
else:
    print ("el numero no tiene el formato esperado")