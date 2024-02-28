#1

sexo = input("Digite F para feminino ou M para masculino: ")
altura = float(input("Digite a altura em metros: "))
peso = 0

if sexo.upper() == "M":
    peso = (72.7 * altura) - 58
elif sexo.upper() == "F":
    peso = (62.1 * altura) - 44.7

if peso != 0:
    print("O peso ideal para sua altura seria %.2f kg" % peso)
else:
    print("Gênero inválido!")