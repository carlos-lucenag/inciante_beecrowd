#ler: distancia total percorrida (Km), total de combustivel gasto (L)
#saida: '(consumo medio [3 casas decimais]) km/l'

x = float(input())
y = float(input())

consumo_medio = x / y

print(f'{consumo_medio:.3f} km/l')
