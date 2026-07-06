#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar 
#que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes 
print('\n\033[0;33m====== DESAFIO 42 ======\033[m')

n1=float(input('\nDigite o primeiro seguimento:'))
n2=float(input('Digite o primeiro seguimento:'))
n3=float(input('Digite o primeiro seguimento:'))
if   n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2: 
    if n1==n2==n3: print('\nOs segmentos pode formar um triangulo equilátero\n')
    elif n1==n2 or n1==n3 or n2==n3: print('\nOs segmentos pode formar um triângulo isósceles\n')
    else: print('\nOs segmentos pode formar um triânglo escaleno\n')

else: print('\nOs segmentos acima não pode formar triangulo\n')