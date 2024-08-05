a = float(input("Digite a altura da parede :"))
l = float(input("Digite a largura da parede :"))

aq = a * l
d = aq / 2
print(20 * "-=-")
print("A sua parede tem {:.2f}²".format(aq))
print("E voce precisa de {:.2f} litros de tinta para pintar a sua parede! ".format(d))
print(20 * "-=-")