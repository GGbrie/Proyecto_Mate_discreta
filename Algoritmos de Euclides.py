print("---- Programa que resuelve problemas de Algoritmos de Euclides ----")
print(" ")
print("               -- Cual es tu problema? --     ")
print(" ")
print("              Formula: a = b * c + r    ")
print(" ")
print("           Ejemplo: 120 = 18 * 6  + 12 ")
print("                    18 = 12 * 1 + 6 ")
print("                     12 = 6 * 2 + 0          MCD = 6")
print(" ")
print("Escribe una cantidad en a = ?")
print("Escribe una cantidad en b = ?")
print("Lego coloca mcd(a,b) ")

def mcd(a, b):
    if b == 0:
        return 0,1,0
 
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1

    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1

        a = b
        b = r

        u0 = u1
        u1 = u
        v0 = v1
        v1 = v

    return a, " -- Problema resulto -- "
      
