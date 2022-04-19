# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavra = ('aprender', 'programar', 'linguagens', 'python',
           'curso', 'estudar', 'praticar', 'trabalhar',
           'mercado', 'programador', 'futuro')

for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')