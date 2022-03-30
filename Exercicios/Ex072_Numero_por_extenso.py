# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa
# deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num in range(0, 21):
        print(f'Você digitou o número {contagem[num]}')
        break
    else:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
