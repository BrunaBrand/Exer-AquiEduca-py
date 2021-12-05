# 7° Crie um programa que calcule um MMC

valor1 = int(input("Informe um valor: "))
valor2 = int(input("Informe outro valor :"))


num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

if num1 > num2:
    maior = num1
else:
    maior = num2
while True:
    if maior % num1 == 0 and maior % num2 == 0:
        print(maior)
        break
    else:
        maior += 1


# ou


num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

if num1 > num2:
    maior = num1
else:
    maior = num2

while maior % num1 != 0 or maior % num2 != 0:
    maior += 1
print(maior)

