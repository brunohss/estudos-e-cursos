print('\033[0;33m====== DESAFIO 27 ======\033[m')
nome=str(input('Digite o seu nome : ')).strip()
dividido=nome.split()
ultimo=int(len(dividido))-1
print(f'O seu primeiro nome : {dividido[0]}\nO seu ultimo nome : {dividido[ultimo]}')