#ler: nome do vendedor, salario fixo, total de vendas efetuadas no mes (em dinheiro)
#15% de comissão sobre as vendas
#saida: TOTAL = R$ (salario fixo + valor da comissao total[duas casas decimais])

nome = input()
salario = float(input())
vendas = float(input())

total = salario + (vendas * 0.15)

print(f'TOTAL = R$ {total:.2f}')