#2

qtdNumerosPares = 0
qtdNumerosImpares = 0
somaPares = 0
somaImpares = 0
mediaPares = 0
mediaGeral = 0

while (True):
    nPositivo = int(input("Digite um número positivo: "))

    if (nPositivo == 0):
        break
    elif (nPositivo % 2 == 0):
        qtdNumerosPares += 1
        somaPares += nPositivo
    elif (nPositivo % 2 ==1):
        qtdNumerosImpares += 1
        somaImpares += nPositivo

nTotal = somaPares + somaImpares
mediaPares = somaPares / qtdNumerosPares
mediaGeral = nTotal / (qtdNumerosPares + qtdNumerosImpares)

print("O total de números digitados é %d e a média geral de números é %d " % (qtdNumerosPares + qtdNumerosImpares, mediaGeral))
print("O total de números pares digitados é %d e a média de números pares é %d " % (qtdNumerosPares, mediaPares))