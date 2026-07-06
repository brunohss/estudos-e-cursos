#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.




print('\n\033[0;33m====== DESAFIO 54 ======\033[m')
nome=[]
idade=[]
for c in range (1,8,1):
    print(f'Pessoa numero {c}')
    nome1 =str(input(f'digite o nome: '))
    nome.append(nome1)
    idade1 =int(input(f'Digite a idade'))
    idade.append(idade1)
pairs = zip(d.values(), d.keys())
list(zip(nome,idade))    
print(nome)
print(idade)