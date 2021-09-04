# Curso: Python Fundamentos Proway
# Aula: Dia 2 - Parte 3 - 2
# Assunto: Dicionários 
# Data: 2021-09-04

#Dicionario =

lista = ['Wanderlei']
tuplas = ('Wanderlei') 
lista[0]
tuplas[0]

#Criando um dicionario
dicionario = {'nome':'Wanderlei', 'sobrenome':'Cardoso Bittencourt','idade':39}

#Lendo dados de um dicionario
print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])

#Alterando dados de um dicionario
dicionario['nome'] = 'Pedro'
dicionario['sobrenome'] = 'Cesar'
dicionario['idade'] = 25

#Lendo os dados alterados
print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])

#adicionando um novo conjunto de chave:valor
dicionario['cpf'] = '1234567890'
print(dicionario['cpf'])

cliente = {}
cliente2 = {'nome':'', 'sobrenome':'', 'idade':0}

cliente['nome'] = input('Digite seu nome: ')
cliente['sobrenome'] = input('Digite sobrenome: ')
cliente['idade'] = int(input('Digite sua idade: '))

print(cliente)
#deletando uma chave de um dicionario
del(cliente['idade'])
print(cliente)

cliente2['nome'] = input('Digite seu nome: ')
cliente2['sobrenome'] = input('Digite sobrenome: ')
cliente2['idade'] = int(input('Digite sua idade: '))

clientes = [cliente, cliente2]
print(clientes)

