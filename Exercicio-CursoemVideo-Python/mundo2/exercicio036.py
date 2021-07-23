# programa para aprovar emprestimos bancario
# valor da casa
valor_casa = float(input('Qual o valor da casa: '))

# salario do comprador
salario = float(input('Qual o seu salário: '))

# quantos anos ele vai pagar
anos_financiamento = int(input('Quantos anos você quer finaciar? '))

# calcular a conversão de anos para meses e o valor da prestação mensal
prestacao_mensal = valor_casa / (anos_financiamento * 12)

# condição que não pode exceder 30% do salario 
if prestacao_mensal <= salario * 0.30:
    print(f'Para pegar uma casa de RS{valor_casa:.2f} em {anos_financiamento} anos, a prestação será R${prestacao_mensal:.2f}')
    print('Emprestimo Aprovado!')

else:
    print(f'Para pegar uma casa de RS{valor_casa:.2f} em {anos_financiamento} anos, a prestação será R${prestacao_mensal:.2f}')
    print('Emprestimo Negado!')