# programa que ler numero inteiro, e usuario escolhe qual base de conversão irá escolher
numero = int(input('Escolha um numero inteiro: '))

print('''Escolha uma das bases para conversão:
[1] converte para binário
[2] converte para octal
[3] converte para hexadecimal''')

opcao = int(input('Sua opção: '))
# condição par 1 - para binario
if opcao == 1:
    print('O número {} convertido para Binário é {}'.format(numero, bin(numero)))

# condição para 2 - para Octal
elif opcao == 2:
    print('O número {} convertido para Octal é {}'.format(numero, oct(numero)))

# condição para 3 - para Hexadecimal
elif opcao == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(numero, hex(numero)))

# Opção se caso não corresponda ao numero de 1 a 3
else:
    print('Opção Invalida!')