print(" ---- //Problema que resuelve Unión de Conjuntos// ---- ")
print("---- El orden en la que se conformaran sera el siguiente ---- ")
print("    A: {a, 2, c, 3, e, 4,  g, 5,  i, 6,  k, 7,  m}  ")
print("Orden: {1, 2, 8, 3, 9, 4, 10, 5, 11, 6, 12, 7, 13} ")
print(" ")
print("    B: {a,  b, c,  d, e,  f,  g,  h, i}" )
print("Orden: {1, 14, 8, 15, 9, 16, 10, 17, 11}" )

lista1=[1,2,8,3,9,4,10,5,11,6,12,7,13]
lista2=[1,14,8,15,9,16,10,17,11]

A=set(lista1)
B=set(lista2)

diferenciaAmenosB= A - B


print("El resultado de la Diferencia de A - B es de:",diferenciaAmenosB)
print("Que Segun el Orden Serian: ---- 2, 3, 4, 5, 6, k, m ----")
