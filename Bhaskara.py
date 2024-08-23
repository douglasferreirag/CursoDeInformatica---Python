import math


a = float(input("Digite o valor de a: "))

b = float(input ("Digite o valor de b: "))

c = float(input("Digite o valor de c: "))

if (a > 0) and (b > 0) and (c > 0):

    delta = (math.pow(b,2.0)) - (4 * a * c)

    if (delta > 0): 

        print("A equação tem duas raízes reais e distintas.")

        raiz1 = ( (-b) + (math.sqrt(delta)) ) / (2 * a)

        raiz2 = ( (-b) - (math.sqrt(delta)) ) / (2 * a)

        print(f'As raízes da equação são: {raiz1}  e {raiz2} ')

    if(delta == 0):

        print("A equação possui raízes reais e iguais.")

        raiz1 = ( (-b) + (math.sqrt(delta)) ) / (2 * a)

        raiz2 = ( (-b) - (math.sqrt(delta)) ) / (2 * a)

        print(f'As raízes da equação são: {raiz1}  e {raiz2} ')

    if(delta < 0):

        print("A equação não possui raízes reais.")

