nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

#Murilo
#012345

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    
    if ' ' in nome:
        print('O seu nome contém espaços.')
    else:
        print('O seu nome não contém espaços')

    print(f'Seu nome contém {len(nome)} letras.')
    print(f'A primeira letrra do seu nome é {nome[0]}.')
    print(f'A últma letra do seu nome é {nome[-1]}.')
else:
    print('Desculpe, você deixou campos vazios.')