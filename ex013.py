s = float(input("Digite o seu salario R$:"))

calc = (s * 15) /100
nv = calc + s
print(30 * "-=-")
print("Esse ano o seu aumento foi de 15% e agora voce vai receber R${:.2f}".format(nv))