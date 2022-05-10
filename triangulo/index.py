#Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
#Perimetro = XX.X
#Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
#Area = XX.X

#area do trapezio = ((B + b) * h) / 2

'''
condição de existência de um triângulo:
lados = a, b, c
a = 16 | b = 20 | c = 30

a + b > c
a + c > b
b + c > a
'''

entrada = input()
entrada = list(entrada.split())

a, b, c = float(entrada[0]), float(entrada[1]), float(entrada[2])

if (a + b) > c and (a + c) > b and (b + c) > a:
    perimetro = a + b + c
    saida = f'Perimetro = {perimetro:.1f}'
else:
    area = ((a + b) * c) / 2
    saida = f'Area = {area:.1f}'

print(saida)
