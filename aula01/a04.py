#Crie um sistema para cadastro de pessoa.
#o sistema deve pedir o nome, idade e sexo.
#cada dado deve ser armazenado em uma variável.
#ao final, o programa deve imprimir uma frase com os dados do usuario.

print('-'*40,'Sistema de Cadastro de Pessoas','-'*40)
print('\n'*2)
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo: ')
print('\n'*2)
print ('Pessoa Cadastrada com Sucesso!\n' , nome, idade, sexo)
