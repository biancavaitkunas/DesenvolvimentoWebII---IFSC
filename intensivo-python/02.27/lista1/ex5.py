produtos = []

def criar_produto():
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria: (1, 2 ou 3)")
    valor = float(input("Digite o valor do produto: "))
    produto = {'nome': nome, 'categoria': categoria, 'valor': valor}
    return produto

def calcula_imposto(produto):
    imposto = 0
    if (produto['categoria'] == '1'):
        imposto = produto['valor'] * 0.1
    elif (produto['categoria'] == '2'):
        imposto = produto['valor'] * 0.2
    else:
        imposto = produto['valor'] * 0.4
        
    return imposto


while (True):

    produtos.append(criar_produto())

    continuar = input("Digite 0 para sair: ")
    if (continuar == '0'):
        break

for p in produtos:
    print("Produto: " + p['nome'], "Categoria: " + p['categoria'], "Valor: " + str(p['valor']), "Imposto: " + str(calcula_imposto(p)))