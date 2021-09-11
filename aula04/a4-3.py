# Curso: Pytho Fundamentos Proway
# Aula: Dia 4 -Parte 4-3
# Assunto: Criando arquivos - A
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, que pode ter o caminho da pasta
# Segundo arquivo é o tipo de abertura
# 'A'- se o arquivo nao existir, cria. Caso exista, adiciona o conteudo no final do arquivo
arquivo = open('aula04\categoria.txt', 'a')
arquivo.write('Categoria 1\n')# utiliza \n para pular de linha
arquivo.close()