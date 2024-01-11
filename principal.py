from Rcadastro import Rcadastro
from title import title
from time import sleep

title('DADOS CADASTRAIS', 34)
cp = 32

        if x == 1:
            print('-' * 40)
            Rcadastro(x, cp)
            print('-' * 40, '\n\033[34m')
        elif x == 2:
            print('-' * 40)
            Rcadastro(x, cp)
            print('-' * 40, '\n\033[34m')
        elif x == 3:
            print('-' * 40)
            Rcadastro(x, cp)
            print('-' * 40, '\n\033[34m')
        elif 4 < x or x < 1:
            print('\033[31m-' * 40)
            print('Opção inválida, digite novamente!')
            print('-' * 40, '\n\033[34m')
        else:
            print('Finalizando programa', end=''), sleep(0.5)
            for z in range(0, 3):
                print('.', end=''), sleep(0.5)
