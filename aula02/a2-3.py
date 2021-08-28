# Curso: Python Fundamentos Proway
# Aula: Dia 2 - Parte 3
# Assunto: Listas , Tuplas, Dicionários
# Data: 2021-08-28

bebidas = ['Coca-cola','cerveja','refri','agua']
print( bebidas[1] ) #segundo elemento da lista
print( bebidas[3] ) #quarto elemento da lista
print( bebidas[1:] ) #ate o final
print( bebidas[:3] ) #do inicio ate o terceiro elemento da lista

bebidas.append("Corona")
print(bebidas)
bebidas[3] = "vodka"
print(bebidas)
bebidas.remove('cerveja')
print(bebidas)
bebidas.pop(-1)
print(bebidas)
ultima_bebida = bebidas.pop(-1)
print(ultima_bebida)
print(bebidas)
#inserir
bebidas.insert(0, 'Refri')
bebidas.insert(2, 'Café')
print(bebidas)
#deleta um dado ou intervalo de dados de uma lista
del(bebidas[1:3])
print(bebidas)


