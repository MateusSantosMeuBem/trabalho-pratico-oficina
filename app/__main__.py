"""Esse é o arquivo onde roda a parte principal do nosso projeto
"""

from utils import (
    dividir,
    multiplicar,
    somar,
    subtrair
)

opcoes_do_menu: list[str] = [
    'Somar dois numero',
    'Subtrair dois numero',
    'Multiplicar dois numeros',
    'Dividir dois numeros',
    'Sair'
]

escolha_do_usuario: int = 0
numero_1: float = 0
numero_2: float = 0

while escolha_do_usuario != 5:
    print('\n'.join([f'[{numero_opcao}] - {opcao}' for numero_opcao, opcao in enumerate(opcoes_do_menu, start = 1)]))
    escolha_do_usuario = int(input('Sua opção: '))

    # FUNÇÃO SOMA
    if escolha_do_usuario == 1:
        numero_1 = float(input('Digite o valor do número 1: '))
        numero_2 = float(input('Digite o valor do número 2: '))
        # -- AQUI ENTRA A FUNÇÃO --

    # FUNÇÃO SUBTRAIR
    elif escolha_do_usuario == 2:
        numero_1 = float(input('Digite o valor do número 1: '))
        numero_2 = float(input('Digite o valor do número 2: '))
        # -- AQUI ENTRA A FUNÇÃO --

    # FUNÇÃO MULTIPLICAR
    elif escolha_do_usuario == 3:
        numero_1 = float(input('Digite o valor do número 1: '))
        numero_2 = float(input('Digite o valor do número 2: '))
        # -- AQUI ENTRA A FUNÇÃO --

    # FUNÇÃO DIVIDIR
    elif escolha_do_usuario == 4:
        numero_1 = float(input('Digite o valor do número 1: '))
        numero_2 = float(input('Digite o valor do número 2: '))
        # -- AQUI ENTRA A FUNÇÃO --

    # SAIR DO PROGRAMA
    elif escolha_do_usuario == 5:
        break
    else:
        print('[OPÇÃO INVÁLIDA!]')
    print()