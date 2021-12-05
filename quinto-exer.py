# 5° Crie um programa que receba um número e diga se é par ou ímpar;

n = float(input("Informe um valor: "))
resto = n % 2

if resto == 0:
    print("Esse número é par")
else:
    print("esse número é impar")