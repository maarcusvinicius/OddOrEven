from random import randint
print('-=' * 15)
print('VAMOS JOGAR \033[0;32mPAR\033[m OU \033[0;31mÍMPAR\033[m')
print('-=' * 15)
count = 0
while True:
    v = int(input('Digite um valor: '))
    vcomput = randint(0, 10)
    soma = v + vcomput
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {v} e o computador {vcomput}. Total de \033[0;0;1m{soma}\033[m')
    print('DEU \033[0;32mPAR\033[m' if soma % 2 == 0 else ('DEU \033[0;31mÍMPAR\033[m'))
    if tipo == 'P':
        if soma % 2 == 0:
            print('-' * 30)
            print('Você \033[0;32;1mVENCEU!\033[m')
            print('-' * 30)
            count += 1
        else:
            print('-' * 30)
            print('Você \033[0;31;1mPERDEU!\033[m')
            print('-' * 30)
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('-' * 30)
            print('Você \033[0;32;1mVENCEU!\033[m')
            print('-' * 30)
            count += 1
        else:
            print('-' * 30)
            print('Você \033[0;31;1mPERDEU!\033[m')
            print('-' * 30)
            break
    print('Vamos jogar novamente...')
print(f'\033[0;31mGAME OVER.\033[m Você ganhou \033[0;32;1m{count} vezes\033[m')