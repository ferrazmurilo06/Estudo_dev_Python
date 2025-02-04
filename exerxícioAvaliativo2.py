numero = input('Digite um número: ')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('Esse número é par')
    else:
        print('Esse número é ímpar.')
except:
    print('Você não digitou um número')

print("------------------------------------------")

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
    else:
        print('Horario inexistente.')
except:
    print('Você não digitou um número inteiro.')

print("------------------------------------------")

nome = input("Digite seu nome:")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é curto!")
elif tamanho_nome >= 5 and tamanho_nome <=6:
    print("Seu nome tem tamanho normal kkk.")
else:
    print('Seu nome é muito grande!')