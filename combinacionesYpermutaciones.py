import math

def main():
  n = int(input("Introducir el Número de Elementos n!: "))
  r = int(input("Introducir el Número de Agrupaciones r!: "))
  
  modo = input("Presione [c] para ver el Resultado Final: ")

  if modo.lower().startswith('c'):
    modo = "combinacion"

  cides = abcde(r, n, modo)
  if modo == "combinacion":
    print(("El resultado de la Combinacion es:",cides))

def abcde(r,n,modo):
    if modo == "combinacion":
        cides= math.factorial (n) // (math.factorial (n-r) * math.factorial (r))
        print(" ")
        print(" ---- n! ----")
        print(math.factorial (n))
        print(" ---- r! ----")
        print(math.factorial (n-r))
        print(" ")
        print(" 2 * 6,227,020,800 = 12,454,41,600")
        print(" ")
        print(" 1,307,674,368,000/12,454,041,600 = ",cides)
        print(" ")
    return cides

if __name__ == '__main__':
    main()
    input()

