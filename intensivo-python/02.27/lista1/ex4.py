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

arquivo = open('clientes.txt', 'w')


for c in clientes:
    arquivo.write(c[0] + ',' + c[1] + ',' + c[2] + '\n')

arquivo.close()