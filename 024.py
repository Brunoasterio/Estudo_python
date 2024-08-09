# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome da sua cidade: ")).strip().upper()[0]

if cidade in "SANTOsanto"[0]:
    print(15 * "-=-")
    print("A cidate tem o nome Santo no começo!")
    print(15 * "-=-")
else:
    print(15 * "-=-")
    print("A cidade não tem o nome Santo no começo! ")
    print(15 * "-=-")