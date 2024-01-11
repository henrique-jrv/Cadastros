def Rcadastro(cp=0):
    import json
    men = 0
    while men != 4:
        print(f"\033[34mAqui você pode cadastrar a pessoa desejada para deixar salvo."
              f"\nCADASTRAR \t[1]"
              f"\nCADASTROS \t[2]"
              f"\nEDITAR \t{'[3]':>7}"
              f"\nSAIR \t{'[4]':>7}")
        men = 0
        while 4 < men or men < 1:
            print('\033[32m')
            while True:
                try:
                    men = int(input('Digite sua opção: '))
                except ValueError:
                    print('\033[31m-' * 40)
                    print('Opção inválida, digite novamente!')
                    print('-' * 40, '\n\033[32m')
                else:
                    break

        with open('C:/Users/joaoh/PycharmProjects/pitõesinhos/Rarmazenamento.json', 'r') as dados:
            x = json.load(dados)
        if men == 1:
            print('-' * 40)
            while True:
                nome = input('Nome: ').title()
                xn = nome.split()
                z = 0
                for y in range(0, len(xn)):
                    if not xn[y].isalpha():
                        z += 1
                if z == 0:
                    break
                else:
                    print(f'\033[31mNome inserido de forma incorreta!\033[{cp}m\n')
            x["nome"].append(nome)
            while True:
                try:
                    x["idade"].append(int(input('Idade: ')))
                except ValueError:
                    print('\033[31Idade inserida de forma incorreta!\033[{cp}m\n')
                else:
                    print('\nDados registrados')
                    break
            with open('C:/Users/joaoh/PycharmProjects/pitõesinhos/Rarmazenamento.json', 'w') as dados:
                json.dump(x, dados)
            print('-' * 40, '\n\033[34m')
        elif men == 2:
            print('-' * 40)
            nu = len(x['nome'])
            for y in range(0, nu):
                print(f'{y + 1}- {x["nome"][y]}, {x["idade"][y]}', 'anos' if x["idade"][y] > 1 else 'ano')
            print('-' * 40, '\n\033[34m')
        elif men == 3:
            print('-' * 40, '\n\033[34m')
            nu = len(x['nome'])
            for y in range(0, nu):
                print(f'{y + 1}- {x["nome"][y]}, {x["idade"][y]} anos')
            while True:
                try:
                    t = int(input('\nDigite o número de quem você deseja editar: '))-1
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
                for y in range(0, len(xn)):
                    if not xn[y].isalpha():
                        z += 1
                if z == 0:
                    break
                else:
                    print(f'\033[31mNome inserido de forma incorreta!\033[{cp}m\n')
            if nome != '00':
                x["nome"][t] = nome
            while True:
                try:
                    save = x["idade"][t]
                    x["idade"][t] = (int(input('\nAtualize a idade (Digite 00 para não alterar): ')))
                    if x["idade"][t] == 00:
                        x["idade"][t] = save
                        break
                except ValueError:
                    print('\033[31Idade inserida de forma incorreta!\033[{cp}m\n')
                else:
                    print('\nDados registrados')
                    break
            with open('C:/Users/joaoh/PycharmProjects/pitõesinhos/Rarmazenamento.json', 'w') as dados:
                json.dump(x, dados)
            print('-' * 40, '\n\033[34m')
