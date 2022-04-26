# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores
# em uma mesma estrutura, acessíveis por chaves individuais.


num = [2, 5, 9, 1]
print(num)
num[2] = 3 # Trocar o objeto na lista
print(f'ex01{num}')
num.append(7) # Adicionar na lista
print(f'ex02{num}')
num.sort() # Coloca na ordem crescente
print(f'ex03{num}')
num.sort(reverse=True)
print(f'ex04{num}')
print(f'Essa lista tem {len(num)} elementos') # quantos elementos tem na lista
num.insert(2, 0) # Adicionar e escolhar o lugar (na posição 2, valor que eu quero inserir)
print(f'ex05{num}')
num.pop() # elimina o último da lista
print(f'ex06{num}')
num.pop(2) # escolho a posição para eliminação
print(f'ex07{num}')
print('-'*30)

num = [2, 5, 9, 1]
print(num)
num[2] = 3 # Trocar o objeto na lista
num.append(7) # Adicionar na lista
num.sort(reverse=True)
num.insert(2, 2) # Adicionar e escolhar o lugar (na posição 2, valor que eu quero inserir)
num.remove(2) # vai eliminar o primeiro 2 que encontrar
print(f'ex08{num}')
print(f'Essa lista tem {len(num)} elementos') # quantos elementos tem na lista
print('-'*30)

num = [2, 5, 9, 1]
print(num)
num[2] = 3 # Trocar o objeto na lista
num.append(7) # Adicionar na lista
num.sort(reverse=True)
num.insert(2, 2) # Adicionar e escolhar o lugar (na posição 2, valor que eu quero inserir)
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o número 4')
print(f'ex09{num}')
print(f'Essa lista tem {len(num)} elementos') # quantos elementos tem na lista
print('-'*30)

# valores = list() pode der escrever assim tb
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')
print('-'*30)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
print('-'*30)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chegeui no final da lista.')
print('-'*30)

a = [2, 3, 4, 7]
b = a # não está fazendo uma cópia, sim uma ligação entre as listas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('-'*30)

a = [2, 3, 4, 7]
b = a[:] # vai criar uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
