#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao tod0 (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome completo:")).strip()

print("Analisando o seu nome...")
print("O seu nome em maiúsculas é [{}]".format(nome.upper()))
print("O seu nome em minúsculas é [{}]".format(nome.lower()))
print("O seu nome tem ao todo [{}] letras ".format(len(nome) - nome.count(" ")))

separa = nome.split()
print("Seu primeiro nome é [{}] e ele tem [{}] letras".format(separa[0], len (separa[0])))