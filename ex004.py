a = input("Digite algo:")

print("O tipo primitivo desse valor é {} ", type(a))
print("Só tem espaços? ", a.isspace())
print("É numerico ? ", a.isnumeric())
print("É alfabetico ? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Está em maiúsculas? ", a.isupper())
print("Está em minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle())