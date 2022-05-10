#Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

entrada = input()
entrada = list(entrada.split())

valor_1, valor_2 = int(entrada[0]), int(entrada[1])

if valor_1 > valor_2:
    maior = valor_1
    menor = valor_2
elif valor_2 > valor_1:
    maior = valor_2
    menor = valor_1
else:
    maior = valor_1
    menor = valor_2

if maior % menor == 0:
    saida = 'Sao Multiplos'
else:
    saida = 'Nao sao Multiplos'

print(saida)
