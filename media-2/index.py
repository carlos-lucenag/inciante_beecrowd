nota_a = float(input())
nota_b = float(input())
nota_c = float(input())

peso_a = 2
peso_b = 3
peso_c = 5

soma_pesos = peso_a + peso_b + peso_c

media = ((nota_a * peso_a) + (nota_b * peso_b) + (nota_c * peso_c)) / soma_pesos

print(f'MEDIA = {media:.1f}')