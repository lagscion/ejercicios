ventas_sem = [  [100, 88, 92, 94, 85, 110, 118],
                [30, 42, 31, 32, 38, 48, 37],
                [23, 35, 39, 45, 55, 60, 61],
                [45, 50, 56, 65, 47, 57, 68],
                [18, 25, 33, 21, 22, 28, 32]]

precio = (1500, 5000, 6500, 2500, 22500)

#pregunta 1 
#que producto que generamas ingresos en la semana

# # total_ing_sem = [0] * 5

# # for fil in range(len(ventas_sem)):
# #     suma = 0
# #     for col in range(len(ventas_sem[fil])):
# #         suma += ventas_sem[fil][col]
# #     total_ing_sem[fil] = suma * precio[fil]

# # ing_mayor = max(total_ing_sem)
# # prod_may_ing = total_ing_sem.index(ing_mayor) + 1

# # print(f"El producto con mas ingreso a la semana es:{prod_may_ing} con $ {ing_mayor:,} ")
# # print(total_ing_sem)
# # ___________________________________________
dia_may_ingr = [0]*7

# for col in range (0,8):
#     suma = 0 
#     for fil in range  (1,6):
#         # suma += ventas_sem [col][0] + ventas_sem [fil]
suma = 0

suma += ventas_sem [0][0] + ventas_sem [1][0]

print (suma)