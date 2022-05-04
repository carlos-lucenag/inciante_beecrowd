#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

entrada = input()
entrada = list(entrada.split())
a, b, c = float(entrada[0]), float(entrada[1]), float(entrada[2])

delta = (b ** 2) + ((-4) * (a * c))

if delta < 0 or a == 0:
    saida = 'Impossivel calcular'
else:
    raiz_1 = ((-b) + (delta ** (1/2))) / (2 * a)
    raiz_2 = ((-b) - (delta ** (1/2))) / (2 * a)
    saida = f'R1 = {raiz_1:.5f}\nR2 = {raiz_2:.5f}'

print(saida)
