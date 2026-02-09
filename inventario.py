"""
construya un programa en python para gestionar un inventario de una ferreteria 
usando diccionarios
"""
def menu():
    print("""*** INVENTARIO FERRETERIA ***
1. agregar profucto
2. consultar producto 
3. actualizar producto 
4. eliminar producto
5. buscar producto por categpria
6. productos con bajo stock
7. valor total del inventario
8. consultar todos los productos 
9. salir""")

def agregar_prod_nuevo():
    print ("\n\n1. agregar producto\n\n")

    cod = input ("codigo del producto: ")
# verificar que ya no exista en el diccionario

if cod in dinv : 
    print(f"error. el producto con codigo {cod} ya existe")
    return dinv



def cargar_datos(dic_inv):
    dic_inv = {
        "mart001": {
            "nombre" : "martillo de cuña",
            "precio" : 15000,
            "stock"  : 25,
            "categoria" : "herramienta"
        },
        
        "dest002" : {
            "nombre" : "desatornillador plano",
            "precio" : 8000,
            "stock" : 40,
            "categoria" : "herramienta"
        },
        "tala003" : {
            "nombre" : "taladro electrico",
            "precio" : 120000,
            "stock" : 40,
            "categoria" : "herramienta electrica"
        }
    }
    return dic_inv



def main ():
    inventario = {}
    
    inventario = cargar_datos(inventario)
    #print (inventario)

    while (True) : 
        menu()
        op = input ("opcion?: ").strip()

        if op =="1":
            inventario = agregar_prod_nuevo(inventario) 
        elif op =="2":
            pass 
        elif op =="3":
            pass 
        elif op =="4":
            pass 
        elif op =="15":
            pass 
        elif op =="6":
            pass
        elif op =="7":
            pass 
        elif op =="8":
            pass 
        elif op =="9":
            print("gracias por usar el programa...")
            break
        else:
