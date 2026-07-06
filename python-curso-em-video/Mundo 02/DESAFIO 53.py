#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
#desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
def compararString(a, b):
    i = 0
    while i < len(a):
        if a[i] != b[i]:
            return False
            break
        i += 1
    return True

#
# Seu teste
#



print('\n\033[0;33m====== DESAFIO 53 ======\033[m')
print('Programa para saber se é primo ou nao')
texto =str(input(f'digite uma frase: '))
invertido = ''
print(f'A frase digitada é : \033[0;32m {texto}\033[m')
for c in range(len(texto)-1,-1,-1):
    invertido += texto[c]

print(f'A frase invertida é: \033[0;32m {invertido}\033[m')
if compararString(texto,invertido):print('\033[0;34mA frase é 100% palindromo')
else: 
    print(f'\033[0;36mremovendos os espaços:\033[m')
    texto=texto.replace(" ", "")
    invertido=invertido.replace(" ", "")
    print(f'Texto digitado: \033[0;31m{texto}\033[m')
    print(f'Texto invertido: \033[0;31m{invertido}\033[m')
    print(f'\033[0;30mEle é um Palindromo removendo os espacos' if compararString(texto,invertido) else f'\033[0;30mO Texto não é palindromo')