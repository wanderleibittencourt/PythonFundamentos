# Curso: Python Fundamentos Proway
# Aula: Dia 3 - Parte 4 - 3
# Assunto: for com dicionarios
# Data: 2021-09-04

produto = {'nome':'cerveja', 'desc':'lager', 'cat':'bebida', 'valor':1.89 }
# imprime todas as chaves do dicionario
for p in produto:
    print(p)

    print('\n')
    # atraves das chaves, imprimindo os valores do dicionario
for p in produto:
    print(produto[p])

print('\n')
# pegando as chaves e valores do dicionario
for (chave, valor) in produto.items():
    print(chave, valor)

