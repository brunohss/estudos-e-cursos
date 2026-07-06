# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário 
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador 
#e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do 
# salário ou então o empréstimo será negado.

print('\033[0;33m====== DESAFIO 36 ======\033[m')


VCasa=float(input('Digite o valor da casa:'))
VSalario=float(input('Digite o valor do salario:'))
Tempo=int(input('Digite o tempo em anos:'))

print(f'O emprestimo será negado. \n devido o seu salario exceder 30% da prestação' if VCasa/(Tempo*12)>=30*VSalario/100 else f'O valor da prestação será R$ {VCasa/(Tempo*12):.2f}')
