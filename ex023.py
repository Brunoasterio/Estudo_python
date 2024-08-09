# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = int(input("Digite um numero:"))

n = str(num)
print(30 * "*")
print("Analisando o numero :{}".format(n))
print(30 * "*")
print(10 * "-=-")
print("Unidade :{} ".format(n[3]))
print("Dezena :{}".format(n[2]))
print("Centena :{}".format(n[1]))
print("Milhar :{}".format(n[0]))
print(10 * "-=-")

