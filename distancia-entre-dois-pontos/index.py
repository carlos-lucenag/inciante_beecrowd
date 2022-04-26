#ler: duas linhas, cada um com dois valores (x e y)
#saida: '(distancia [com 4 casas decimais])'
#formula distancia -> distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

entrada1 = list(input().split())
entrada2 = list(input().split())

x1, y1 = float(entrada1[0]), float(entrada1[1])
x2, y2 = float(entrada2[0]), float(entrada2[1])

distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

print(f'{distancia:.4f}')