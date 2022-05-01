#Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

valor = float(input())

valor_notas = int(valor)
valor_moedas = int(((valor * 10) * 10) - (valor_notas * 100))

lista_valores_notas = [100, 50, 20, 10, 5, 2]
lista_valores_moedas = [100, 50, 25, 10, 5, 1]
lista_qnt_notas = list()
lista_qnt_moedas = list()
qnt_notas = 0
qnt_moedas = 0
cont_notas = 0
cont_moedas = 0

while True:
    if cont_notas == len(lista_valores_notas): break
    if valor_notas >= lista_valores_notas[cont_notas]:
        qnt_notas = valor_notas // lista_valores_notas[cont_notas]
        valor_notas -= qnt_notas * lista_valores_notas[cont_notas]
        lista_qnt_notas.append(qnt_notas)
    else:
        lista_qnt_notas.append(0)
    cont_notas += 1

valor_moedas += valor_notas * 100

while True:
    if cont_moedas == len(lista_valores_moedas): break
    if valor_moedas >= lista_valores_moedas[cont_moedas]:
        qnt_moedas = valor_moedas // lista_valores_moedas[cont_moedas]
        valor_moedas -= qnt_moedas * lista_valores_moedas[cont_moedas]
        lista_qnt_moedas.append(qnt_moedas)
    else:
        lista_qnt_moedas.append(0)
    cont_moedas += 1

saida = f'NOTAS:\n{lista_qnt_notas[0]} nota(s) de R$ 100.00\n{lista_qnt_notas[1]} nota(s) de R$ 50.00\n{lista_qnt_notas[2]} nota(s) de R$ 20.00\n{lista_qnt_notas[3]} nota(s) de R$ 10.00\n{lista_qnt_notas[4]} nota(s) de R$ 5.00\n{lista_qnt_notas[5]} nota(s) de R$ 2.00\nMOEDAS:\n{lista_qnt_moedas[0]} moeda(s) de R$ 1.00\n{lista_qnt_moedas[1]} moeda(s) de R$ 0.50\n{lista_qnt_moedas[2]} moeda(s) de R$ 0.25\n{lista_qnt_moedas[3]} moeda(s) de R$ 0.10\n{lista_qnt_moedas[4]} moeda(s) de R$ 0.05\n{lista_qnt_moedas[5]} moeda(s) de R$ 0.01'

print(saida)
