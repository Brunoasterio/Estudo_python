#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos
# alunos e escrevendo na tela o nome do escolhido.

import random

nome1 = str(input("Digite o seu nome: "))
nome2 = str(input("Digite o seu nome: "))
nome3 = str(input("Digite o seu nome: "))
nome4 = str(input("Digite o seu nome: "))

lista = [nome1, nome2, nome3, nome4]
sorteio = random.choice(lista)

print(10 * "-=-")
print("O aluno escolhido foi [{}]".format(sorteio))
print(10 * "-=-")