with open ('teste.txt', 'w', encoding='utf-8') as arquivo:
arquivo.write('Não precisa colocar o .close()')

with open ('teste.txt', 'r') as arquivo
 linhas = arquivo.readlines()
 for l in linhas:
     l_sem_barra_n = l.strip()
     print(l_sem_barra_n)

