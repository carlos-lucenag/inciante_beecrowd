#carroX = 60km/h
#carroY = 90km/h
#carroY se afasta 1km cada 2min ((1/2)km/min) -> 0.5km/min
#ler: distancia em km (int)
#calcular o tempo necessario para o carroY alcançar essa distancia em relação ao carroX
#saida: '(tempo) minutos'

distancia = int(input())

tempo = distancia / 0.5

print(f'{int(tempo)} minutos')