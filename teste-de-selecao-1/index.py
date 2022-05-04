#Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

entrada = input()
entrada = list(entrada.split())
a, b, c, d = int(entrada[0]), int(entrada[1]), int(entrada[2]), int(entrada[3])

'''
b > c
d > a
c + d > a + b
c, d > 0
a = par
'''

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and (a % 2) == 0:
    saida = 'Valores aceitos'
else:
    saida = 'Valores nao aceitos'

print(saida)
