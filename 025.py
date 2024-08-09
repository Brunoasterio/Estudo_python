# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite o seu nome completo: ")).strip().upper()
if "SILVA" in nome :
    print(15 * "-=-")
    print("Voce tem Silva no nome!")
    print(15 * "-=-")
else:
    print(15 * "-=-")
    print(" Voce não tem Silva no nome!")
    print(15 * "-=-")