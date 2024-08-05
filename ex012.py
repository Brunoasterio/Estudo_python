p = float(input("Digite o valor do produto: "))

calc = (p * 5) /100
desc = p - calc
print("Voce obteve um desconto de 5% e o novo preço ficou R${:.2f} ".format(desc))