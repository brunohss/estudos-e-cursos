print('\033[0;33m====== DESAFIO 24 ======\033[m')
cidade=str(input('Digite o nome da cidade:')).strip()
print(f'A cidade comeca com a palavra santo: { "santo" in (cidade.lower().split()[0])}')
