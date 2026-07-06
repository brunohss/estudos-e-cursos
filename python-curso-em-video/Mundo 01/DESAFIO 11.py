print('\033[0;33m====== DESAFIO 11 ======\033[m')
print('Programa para calcular a quantidade de tinta que precisa para pintar a parede')
print('Utilizando uma tinta o qual cada litro pinta uma area de 2m')
alt=float(input('digita a altura da parede: '))
larg=float(input('digite a largura da parede: '))
area=alt*larg
print('Ira precisar de {:.2f} litros para pintar esta parede'.format(area/2))