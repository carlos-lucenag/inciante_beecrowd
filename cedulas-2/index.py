#este código é uma variação da versão anterior, meu intuito é fazer uma versão mais otimizada usando menos linhas de código e conhecimentos mais avançados
#Ao invés de usar vários ifs e elses eu vou usar uma lista com os valores das notas e uma estrutura de repetição

valor = int(input())
valor_saida = valor

notas = [100, 50, 20, 10, 5, 2, 1]
lista_notas = list()
cont = 0

while True:
    if cont == len(notas): break
    if valor >= notas[cont]:
        qnt_notas = valor // notas[cont]
        valor -= qnt_notas * notas[cont]
        lista_notas.append(qnt_notas)
    else:
        lista_notas.append(0)
    cont += 1

saida = f'{valor_saida}\n{lista_notas[0]} nota(s) de R$ 100,00\n{lista_notas[1]} nota(s) de R$ 50,00\n{lista_notas[2]} nota(s) de R$ 20,00\n{lista_notas[3]} nota(s) de R$ 10,00\n{lista_notas[4]} nota(s) de R$ 5,00\n{lista_notas[5]} nota(s) de R$ 2,00\n{lista_notas[6]} nota(s) de R$ 1,00'

print(saida)