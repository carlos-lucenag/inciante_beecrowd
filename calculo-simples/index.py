#ler: duas linhas, em cada linha -> codigo da peça, numero de peças, valor da peça
#saida: total a pagar

entrada1 = list(input().split())
entrada2 = list(input().split())

codigo1, numero1, valor1 = int(entrada1[0]), int(entrada1[1]), float(entrada1[2])
codigo2, numero2, valor2 = int(entrada2[0]), int(entrada2[1]), float(entrada2[2])

valor_total = (numero1 * valor1) + (numero2 * valor2)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')