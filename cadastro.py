def cadastro(cp=0):
    """
    Função utilizada para criar/editar um cadastro,
    será salvo em outro arquivo e permanecerá lá
    mesmo após o encerramento da função.

    :param cp: Serve para receber o código de cor padrão do sistema,
    caso não tenha preferência, ou prefira a cor padrão digite 0.

    :return: Nenhum
    """
    import json
    from time import sleep

    menu = 0
    while menu != 5:
        print(f"\033[34mAqui você pode cadastrar a pessoa desejada para deixar salvo."
              f"\nCADASTRAR \t[1]"
              f"\nCADASTROS \t[2]"
              f"\nEDITAR \t{'[3]':>7}"
              f"\nEXCLUIR \t[4]"
              f"\nSAIR \t{'[5]':>7}")
        menu = 0
        while 5 < menu or menu < 1:
            print('\033[32m')
            while True:
                try:
                    menu = int(input('Digite sua opção: '))
                except ValueError:
                    print('\033[31m-' * 40)
                    print('Opção inválida, digite novamente!')
                    print('-' * 40, '\n\033[32m')
                except KeyboardInterrupt:
                    menu = 5
                    print()
                    break
                else:
                    if menu > 5 or menu < 1:
                        print('\033[31m-' * 40)
                        print('Opção inválida, digite novamente!')
                        print('-' * 40, '\n\033[32m')
                    else:
                        break

        with open('C:/armazenamento.json', 'r') as dados:
            lista = json.load(dados)
        if menu == 1:
            print('-' * 40)
            while True:
                nome = input('Nome: ').title()
                xn = nome.split()
                z = 0
                for x in range(0, len(xn)):
                    if not xn[x].isalpha():
                        z += 1
                if z == 0:
                    break
                else:
                    print(f'\033[31mNome inserido de forma incorreta!\033[{cp}m\n')
            lista["nome"].append(nome)
            while True:
                try:
                    lista["idade"].append(int(input('Idade: ')))
                except ValueError:
                    print(f'\033[31mIdade inserida de forma incorreta!\033[{cp}m\n')
                else:
                    print('\nDados registrados')
                    sleep(0.7)
                    break
            with open('C:/armazenamento.json', 'w') as dados:
                json.dump(lista, dados)
            print('-' * 40, '\n\033[34m')
        elif menu == 2:
            print('-' * 40)
            num = len(lista['nome'])
            for x in range(0, num):
                print(f'{x + 1}- {lista["nome"][x]}, {lista["idade"][x]}', 'anos' if lista["idade"][x] > 1 else 'ano')
            print('-' * 40, '\n\033[34m')
            sleep(1)
        elif menu == 3:
            print('-' * 40, '\n\033[34m')
            num = len(lista['nome'])
            for x in range(0, num):
                print(f'{x + 1}- {lista["nome"][x]}, {lista["idade"][x]} anos')
            sleep(1)
            while True:
                try:
                    edit = int(input('\nDigite o número de quem você deseja editar: ')) - 1
                except ValueError:
                    print('Opção inválida!')
                else:
                    break
            while True:
                nome = input('\nAtualize o nome (Digite 00 para não alterar): ').title()
                if nome == '00':
                    break
                xn = nome.split()
                z = 0
                for x in range(0, len(xn)):
                    if not xn[x].isalpha():
                        z += 1
                if z == 0:
                    break
                else:
                    print(f'\033[31mNome inserido de forma incorreta!\033[{cp}m\n')
            if nome != '00':
                lista["nome"][edit] = nome
            while True:
                try:
                    save = lista["idade"][edit]
                    lista["idade"][edit] = (int(input('\nAtualize a idade (Digite 00 para não alterar): ')))
                    if lista["idade"][edit] == 00:
                        lista["idade"][edit] = save
                        break
                except ValueError:
                    print(f'\033[31mIdade inserida de forma incorreta!\033[34m\n')
                else:
                    print('\nDados registrados')
                    break
            with open('C:/armazenamento.json', 'w') as dados:
                json.dump(lista, dados)
            print('-' * 40, '\n\033[34m')
        elif menu == 4:
            print('-' * 40, '\n\033[34m')
            for x in range(0, len(lista['nome'])):
                print(f'{x + 1}- {lista["nome"][x]}, {lista["idade"][x]} anos')
            sleep(1)
            while True:
                try:
                    print(len(lista['nome']))
                    ex = int(input('\nDigite o núemro de quem você deseja excluir: '))
                except ValueError:
                    print('\033[31mInformação inserida de forma incorreta!\033[m')
                else:
                    if len(lista['nome']) < ex or ex < 1:
                        print('\033[31mInformação inserida de forma incorreta!\033[34m')
                    else:
                        break
            print(ex)
            lista['nome'].remove(lista['nome'][ex-1]), lista['idade'].remove(lista['idade'][ex-1])
            with open('C:/armazenamento.json', 'w') as dados:
                json.dump(lista, dados)
            print('-' * 40, '\n\033[34m')
        elif menu == 5:
            print('\nFinalizando programa', end=''), sleep(0.5)
            for z in range(0, 3):
                print('.', end=''), sleep(0.5)
