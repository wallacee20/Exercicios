#  programa que compara dois numeros inteiros e Mostra qual valor maior

# pede os valores para o usuário  
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

# condição do primeiro valor é maior
if numero1 > numero2:
    print('O Primeiro numero é maior!')

# condição dos numero iguais
elif numero1 == numero2:
    print('Não existe valor maior, os valores são iguais!')

# condição do segundo valor é maior
else:
    print('O Segundo numero é maior!')