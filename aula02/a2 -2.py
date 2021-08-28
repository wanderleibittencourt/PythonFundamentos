# Curso: Python Fundamentos Proway
# Aula: Dia 2 - Parte 2
# Assunto: While, instruções alinhadas
# Data: 2021-08-28

# repeticoes = 0
# while(repeticoes <=3): #enquanto
#     idade = input('Digite a idade')
#     repeticoes = repeticoes +1

# print('-'*20, 'Cadastro de Clientes', '-'*20)
# print ('\n')
# nome = input('Digite seu nome: ')
# sobrenome = input('Seu Sobrenome: ')
# idade = int(input('Digite sua idade: '))

# invalido = True
# while(invalido):
#     if(idade >= 18):
#         print('Cadastrado com Sucesso!')
#         invalido = False
#     elif(idade > 0):
#         print('Não permitido menores de idade')
#         invalido = False
#     else:
#         print('Idade informada é inválida')
#         idade = int(input('Digite sua idade: ')) 

import os

invalido = True
while(invalido):
    print('-'*20, 'Sistemas de Bebidas', '-'*20,'\n')
    print('\t1-Cadastrar uma bebida')
    print('\t2-Listar bebidas cadastradas')
    print('\t0-Sair')
    opcao = int(input('\nDigite uma opção do menu: '))

    if(opcao < 0 or opcao >2):
        print('Opção invalida!')
        input('Digite enter para continuar...')
        os.system('clear')
    else:
        invalido= False

      