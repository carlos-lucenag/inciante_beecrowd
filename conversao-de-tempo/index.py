#Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
#1s = 1s | 1min = 60s | 1h = 3600s

n = int(input())

valores_unidades_tempo = [3600, 60, 1]
lista_qnt_unidades = list()
cont = 0

while True:
    if cont == len(valores_unidades_tempo): break
    if n >= valores_unidades_tempo[cont]:
        qnt_tempo_unidade = n // valores_unidades_tempo[cont]
        n -= qnt_tempo_unidade * valores_unidades_tempo[cont]
        lista_qnt_unidades.append(qnt_tempo_unidade)
    else:
        lista_qnt_unidades.append(0)
    cont += 1

saida = f'{lista_qnt_unidades[0]}:{lista_qnt_unidades[1]}:{lista_qnt_unidades[2]}'

print(saida)
