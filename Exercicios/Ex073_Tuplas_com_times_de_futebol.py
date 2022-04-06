# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico Paranaense', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'Lista de times do Brasileirão 2021: {times}')
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Times em ordem alfábetica: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º posição')

