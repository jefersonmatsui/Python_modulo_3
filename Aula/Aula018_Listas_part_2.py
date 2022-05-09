# Nessa aula, vamos aprender o que são LISTAS e como utilizar
# listas em Python. As listas são variáveis compostas que permitem
# armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.

print('*-'*30)
print('1° Exemplo')
teste = list()
teste.append('Jeferson')
teste.append(35)
galera = list()
galera.append(teste)
print(galera)

print('*-'*30)
print('2° Exemplo') # Ligação entre as duas estruturas
teste = list()
teste.append('Jeferson')
teste.append(35)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

print('*-'*30)
print('3° Exemplo') # Tem que fazer uma cópia
teste = list()
teste.append('Jeferson')
teste.append(35)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

print('*-'*30)
print('4° Exemplo')
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria',45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])

print('*-'*30)
print('5° Exemplo')
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria',45]]
for p in galera:
    print(p)

print('*-'*30)
print('6° Exemplo')
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria',45]]
for p in galera:
    print(p[0])

print('*-'*30)
print('7° Exemplo')
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[1])

print('*-'*30)
print('8° Exemplo')
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria',45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('*-'*30)
print('9° Exemplo')
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

print('*-'*30)
print('10° Exemplo')
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print((f'{p[0]} é menor de idade.'))
        totmen + 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')