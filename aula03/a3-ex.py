# Exercicio 1 - Aula Funcoes e Procedimentos
# Crie um sistema de cadastro de produtos
# O sistema deve conter 4 funcoes
# 1 - Imprimir um cabecalho
#   utilizar a biblioteca para limpar tela
# 2 - Funcao que solicita os dados do produto
#   usar as funcoes input para solicitar nome, descricao e valor
#   salvar os dados em um dicionario
#   retornar o dicionario ao final da funcao
# 3 - Funcao de validacao de dados
#   deve validar se o nome do produto maior que 5 caracteres
#   validar se o valor maior que zero
# 4 - Imprimir um rodape e os dados do produto cadastrado
import os

def cabecalho():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-'*30, 'Cadastro de Produtos', '-'*30)
    print ('\n')

def cadastra():
    produto = {}
    produto['nome'] = input('Digite o nome: ')
    produto['descricao'] = input('digite a descrição: ')
    produto['valor']  = float(input('Digite o valor: '))
    return produto

# Funcao 3
def valida(produto):
    valido = True
    # valida nome >5
    if( len(produto['nome']) < 5 ):
        print('Nome do produto inválido! deve ser maior que 5')
        valida = False
    # valida valor >0
    if(produto['valor'] < 0):
        print('O valor do produto é invalido! deve ser maior que zero')
        valido = False
    return valido

# Funcao 4
def rodape(produto):
    print('Produto cadastrado com sucesso!')
    print('\t', produto['nome'], produto['descricao'], produto['valor'])    
    
cabecalho()
p = cadastra()
if(valida(p)):
    rodape(p)



