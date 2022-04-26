#ler: na mesma linha, 3 valores float (a, b e c)
'''
pi = 3.14159
calculos:
a) area triangulo retangulo A = base, C = altura -> (a * c) / 2
b) area do circulo de raio C -> pi * (c ** 2)
c) area do trapezio A e B = bases, C = altura -> ((a + b) * c) / 2
d) area do quadrado B = lado -> b ** 2
e) area do retangulo A e B = lados -> a * b
'''
#saida: TRIANGULO: ... CIRCULO: ... TRAPEZIO: ... QUADRADO: ... RETANGULO: ... [deve ter 3 casas decimais]

entrada = list(input().split())
a, b, c = float(entrada[0]), float(entrada[1]), float(entrada[2])

pi = 3.14159

triangulo = (a * c) / 2
circulo = pi * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

saida = f'TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}'

print(saida)
