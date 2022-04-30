#o automovel faz 12km/L -> 1km = 1/12L
#ler: tempo gasto na viagem (int), velocidade media na viagem (int)
#com os dados fornecidos, calcular a distancia percorrida e depois usar o consumo do automovel para chegar ao resultado de quanto seria gasto
#saida: '(litros gastos[3 casas decimais])'
#VM = S/T -> S = VM * T

tempo_gasto = int(input())
velocidade_media = int(input())

distancia_percorrida = velocidade_media * tempo_gasto
consumo_total = distancia_percorrida / 12

print(f'{consumo_total:.3f}')