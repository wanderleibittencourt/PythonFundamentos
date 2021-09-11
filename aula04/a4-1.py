# Curso: Pytho Fundamentos Proway
# Aula: Dia 4 -Parte 4-1
# Assunto: Arquivos
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, que pode ter o caminho da pasta
# Segundo arquivo é o tipo de abertura
# 'w'- se o arquivo nao existir, cria. Caso exista, sobreescreve
arquivo = open('aula04\cliente.txt', 'w')
arquivo.write('cliente1-clientePF')
arquivo.close()