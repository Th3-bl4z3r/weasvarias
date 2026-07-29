def piramide_invertida(n, x):
    if n == 1:
        return " "*x+"*"
    elif n < 1:
        return "ERROR"
    msj = ""
    for k in range(n):
        if k != n-1:
            msj = msj + "*_" 
        else:
            msj = msj + "*"
    print(" "*x + msj)
    return piramide_invertida(n-1, x+1)

print("🔺Pirámides invertidas🔺")
a = int(input("ingresa la base de la pirámide invertida (números enteros positivos): "))
print(piramide_invertida(a, 0))
print("By Bl4z3")
# prime de primes