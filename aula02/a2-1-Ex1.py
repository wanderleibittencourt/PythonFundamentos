# Crie um cadastro de clientes para uma loja de bebidas
# O cadastro deve solicitar ao usuario:
# Nome, Sobrenome e idade
# O sitema deve permitir apenas clientes maiores de idade
# Caso a idade seja menor, informar que nao pode ser cadastrado

print('-'*20, 'Cadastro de Clientes', '-'*20)
print ('\n')
nome = input('Digite seu nome: ')
sobrenome = input('Seu Sobrenome: ')
idade = int(input('Digite sua idade: '))

if(idade >= 18):
    print('Cadastrado com Sucesso!')
elif(idade > 0):
    print('Não permitido menores de idade')
else:
    print('Idade informada é inválida')
print ('\n')
print('-'*20, 'Fim de Transmição', '-'*20)


