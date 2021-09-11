# Curso: Pytho Fundamentos Proway
# Aula: Dia 4 -Parte 4-4
# Assunto: Criando arquivos - R
# Data: 2021-09-11



arquivo = open('aula04\categoria.txt', 'r')
#Readlines = cria uma lista de string com todas as linhas do arquivo
linhas = arquivo.readlines()

for l in linhas:
    l_sem_barra_n = l.strip() # strip remove \n, \t e espacos em branco
    print(l_sem_barra_n)

# Fechando o arquivo
arquivo.close()