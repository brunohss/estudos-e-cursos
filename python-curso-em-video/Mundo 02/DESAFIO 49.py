#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
#só que agora utilizando um laço for.



print('\n\033[0;33m====== DESAFIO 49 ======\033[m')
print('todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500')
n1 =int(input('digite um numero: '))
print(f'Tabuada do {n1}')
for c in range(1,11,1):
    print(f'\033[0;34m {n1} x {c:2} = {n1*c:2}')