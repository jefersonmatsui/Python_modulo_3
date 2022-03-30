# Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
# As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores
# em uma mesma estrutura, acessíveis por chaves individuais.
print('*'*50)
print('Exemplo 1')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
# se tentar atribuir lanche[1] = 'Refrigerante' o progrma vai dar erro
print(f'1 {lanche}')
print(f'2 {lanche[1]}') #[0]'Hamburguer', [1]'Suco', [2]'Pizza', [3]'Pudim'
print(f'3 {lanche[-2]}') #[-4]'Hamburguer', [-3]'Suco', [-2]'Pizza', [-1]'Pudim'
print(f'4 {lanche[1:3]}') #Pedaço da tupla
print(f'5 {lanche[2:]}')
print(f'6 {lanche[:2]}') #vai ignorar os ultimos elementos
print(f'7 {lanche[-2:]}')
print('*'*50)

print('Exemplo 2')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('*'*50)

print('Exemplo 3')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')
print('*'*50)

print('Exemplo 4')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
print('*'*50)

print('Exemplo 5')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) # coloca em ordem e em lista
print(lanche)
print('*'*50)

print('Exemplo 6') # junta tudo
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print('*'*50)

print('Exemplo 7') # quantas vezes aparece o numero
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5))
print('*'*50)

print('Exemplo 8') # onde esta a posição, começando da posição 0
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.index(8))
print('*'*50)

print('Exemplo 9')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.index(5, 1)) # Começando da posição 1
print('*'*50)

print('Exemplo 10')
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
print('*'*50)

print('Exemplo 11')
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # apaga tudo da memória, não dá para apagar apenas um elemento só
print('*'*50)


