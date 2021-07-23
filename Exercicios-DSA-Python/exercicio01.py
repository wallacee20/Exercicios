# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

# pede ao usuário que escreva um dia da semana e armagena na variável semana
dia = str(input('Digite um dia da semana: '))

# condição do usuário digitar (sabado ou domingo)
if dia in 'domingo sabado':
    print('Hoje é dia de descanso!')

# condição do usuário digitar (segunda, terça, quarta, quinta ou sexta)
elif dia in 'segunda terça quarta quinta sexta':
    print('Você precisa trabalhar!')

# condição se caso o usuário digitar outra palavra diferente a um dia da semana 
else:
    print('Semana inexistente!!! escreva um dia da Semana')