# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

listanum = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in listanum:
        listanum.append(valor)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Valor duplicado! Não será adicionado...')
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
listanum.sort()
print(f'Você digitou os valores {listanum}')