#Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
'''
1 - Cachorro Quente  - R$ 4.00
2 - X-Salada         - R$ 4.50
3 - X-Bacon          - R$ 5.00
4 - Torrada Simples  - R$ 2.00
5 - Refrigerante     - R$ 1.50
'''

entrada = input()
entrada = list(entrada.split())

codigo, quantidade = int(entrada[0]), int(entrada[1])

lista_precos = [4.00, 4.50, 5.00, 2.00, 1.50]

for i in range(0, (len(lista_precos) + 1)):
    if codigo == i:
        preco = lista_precos[(i - 1)]
        break

total = preco * quantidade

saida = f'Total: R$ {total:.2f}'

print(saida)
