#ler: 3 valores na mesma linha, int(a, b e c)
#formula maior entre 2 valores -> maior_ab = (a + b + abs(a-b)) / 2
#saida: '(maior) eh o maior'

entrada = list(input().split())
a, b, c = int(entrada[0]), int(entrada[1]), int(entrada[2])

maior_ab = (a + b + abs(a - b)) / 2
maior = (maior_ab + c + abs(maior_ab - c)) / 2

'''
if a > b:
    maior = (a + c + abs(a - c)) / 2
elif b > a:
    maior = (b + c + abs(b - c)) / 2
elif a == b:
    maior = (a + c + abs(a - c)) / 2
    if a == c:
        maior = a
'''

print(f'{int(maior)} eh o maior')
