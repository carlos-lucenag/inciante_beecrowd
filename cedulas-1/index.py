#Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

valor = int(input())
valor_saida = valor

if valor >= 100:
    notas_100 = valor // 100
    valor -= (notas_100 * 100)
else:
    notas_100 = 0

if valor >= 50:
    notas_50 = valor // 50
    valor -= (notas_50 * 50)
else:
    notas_50 = 0

if valor >= 20:
    notas_20 = valor // 20
    valor -= (notas_20 * 20)
else:
    notas_20 = 0

if valor >= 10:
    notas_10 = valor // 10
    valor -= (notas_10 * 10)
else:
    notas_10 = 0

if valor >= 5:
    notas_5 = valor // 5
    valor -= (notas_5 * 5)
else:
    notas_5 = 0

if valor >= 2:
    notas_2 = valor // 2
    valor -= (notas_2 * 2)
else:
    notas_2 = 0

if valor >= 1:
    notas_1 = valor // 1
    valor -= (notas_1 * 1)
else:
    notas_1 = 0

saida = f'{valor_saida}\n{notas_100} nota(s) de R$ 100,00\n{notas_50} nota(s) de R$ 50,00\n{notas_20} nota(s) de R$ 20,00\n{notas_10} nota(s) de R$ 10,00\n{notas_5} nota(s) de R$ 5,00\n{notas_2} nota(s) de R$ 2,00\n{notas_1} nota(s) de R$ 1,00'

print(saida)