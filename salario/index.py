#ler: NUM DO FUNCIONÁRIO | NUM DE HORAS TRABALHADAS | VALOR RECEBIDO POR HORA
#saida: NUM DO FUNCIONÁRIO -> 'NUMBER = (número)'
#     SALÁRIO -> 'SALARY = U$ (salário [com duas casas decimais])'

numero = int(input())
qnt_horas_trabalhadas = int(input())
valor_por_hora = float(input())

salario = qnt_horas_trabalhadas * valor_por_hora

saida = f'NUMBER = {numero}\nSALARY = U$ {salario:.2f}'
print(saida)