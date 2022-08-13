# Módulo 1
from datetime import datetime
import random

print('---------- Olá, bem-vindo a nossa empresa ---------')
nome_usuario = input('Digite seu nome: ')
idade_usuario = int(input('Qual sua idade: '))
data_cadastro = datetime.now()
cartoes = ['50,00', '250,00', '120,00']
cartao = random.choice(cartoes)
data_nascimento = datetime.strptime(
    input('Digite sua data de aniversario no formato dd/mm/aaaa: '), '%d/%m/%Y')

# Módulo 2
print(f'Olá {nome}, seu registro foi concluido com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.\n Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}')
