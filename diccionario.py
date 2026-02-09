#diccionaario vacio
dicc= {}
dicc = dict ()  

#asignar valores 

camper = {"nombre": "sebastian",
          "edad"  :  "18",
          "carrera": "ing.sistemas"
          }

producto = dict(nombre= "portatil", precio = 400_000, stock = 10)

#pares

pares = [("a",1), ("b",2), ("c", 3)]
diccionario = dict(pares)

#acceso

print(camper["nombre"])
print ( camper.get("edad"))
print (camper.get("pasatiempo", "pingpong"))

#metodo keys(): 
print(camper.keys())

camper ["pasatiempos"] = "fubol"

#metodo values(): devuelve todos los valores
print(camper.values())

#metodo items ():  devuelve todos los pares clave y tupla 
print(camper.items())

#recorrer
#con keys

for key in camper.keys():
    print(f"camper[{key}]-> {camper[key]}", end=", ")
#2 . con items
for llave, valor in camper.items():
    print (f"camper[{llave}]-> {valor}", end=", ")

#pop(): elimina un aclave y retorna su valor
camper ["pasatiempo"] = ("futbol, programar")
print(camper.pop("pasatiempos"))
print(camper)

#pop item(): elimina y retorna el ultimo par clave valor insertado

print(camper.popitem())
print(camper)

#clear(): elimina todos los elementos del diccionario
#camper.clear()
#camper = {}

#copy(): crea un acopia  del diccionario
camper_backup= {}
camper_backup= camper.copy()
print(camper_backup)

#setdefault(): retorna el valor de una clave. sino existe la crea con un valor por defecto
camper.setdefault("pasatiempo", ["futbol", "programar", "parrandear"])
print(camper)
print(camper.setdefault("pasatiempo", "dormir"))

#len(): cantidad de pares valor que hay en el diccionario
print(len(camper))

#in: verifica si existe una llave en el diccionario
print("sexo" in camper)

#del(): elimina una llave
del camper["pasatiempo"]

#any(): verifica si almenos un valor de la llave es verdadero

camper ["sueldo"] = 0
print (any(camper)) # ->true

#all(): verificasi todos los valores de la llave es verdadero

print(all(camper)) #-> false
