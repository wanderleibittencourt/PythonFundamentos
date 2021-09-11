# Curso: Pytho Fundamentos Proway
# Aula: Dia 3 -Parte 3-1
# Assunto: Funcoes e procedimentos
# Data: 2021-09-11

import os

# Imprimindo cabecalho
def imprimir_cabecalho():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-'*20, 'Cadastro de Clientes', '-'*20)
    print ('\n')

# entrada usuario
def cadastra_usuario():
    nome = input('Digite seu nome: ')
    sobrenome = input('Seu Sobrenome: ')
    idade = int(input('Digite sua idade: '))
    usuario = {'nome': nome, 'sobrenome': sobrenome, 'idade': idade}
    return usuario

# validacao de cadastro
def valida_usuario(idade):
    if(idade >= 18):
        print('Cadastrado com Sucesso!')
    elif(idade > 0):
        print('Não permitido menores de idade')
    else:
        print('Idade informada é inválida')

imprimir_cabecalho()
u =cadastra_usuario()
valida_usuario(u['idade'])
