#Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
#Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

idade_em_dias = int(input())

lista_qnt_dias = [365, 30, 1]
lista_resultados = list()
resultado = 0
cont = 0

while True:
    if cont == len(lista_qnt_dias): break
    if idade_em_dias >= lista_qnt_dias[cont]:
        resultado = idade_em_dias // lista_qnt_dias[cont]
        idade_em_dias -= resultado * lista_qnt_dias[cont]
        lista_resultados.append(resultado)
    else:
        lista_resultados.append(0)
    cont += 1

saida = f'{lista_resultados[0]} ano(s)\n{lista_resultados[1]} mes(es)\n{lista_resultados[2]} dia(s)'

print(saida)
