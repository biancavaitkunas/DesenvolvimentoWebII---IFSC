clientes = []

while (True):

    cliente = []
    cliente.append(input("Digite o nome: "))
    cliente.append(input("Digite o cpf: "))
    cliente.append(input("Digite o telefone: "))

    clientes.append(cliente)

    continuar = input("Digite 0 para encerrar: ")

    if (continuar == '0'):
        break


for c in clientes:
    print("Nome : %s, CPF: %s, Telefone: %s" % (c[0], c[1], c[2]))