#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

numero = float(input("Digite um numero com virgula(OBS:No lugar da virgula, utilize o ponto(.):"))

print("O valor digitado foi [{}] e a sua porção inteira é [{}]".format(numero, int(numero)))