#ler: raio
#formula volume da esfera = (4/3) * pi * (raio ** 3)
#pi = 3.14159
#saida: VOLUME = (volume [com 3 casas decimais])

raio = float(input())

pi = 3.14159

volume = (4/3) * pi * (raio ** 3)

print(f'VOLUME = {volume:.3f}')