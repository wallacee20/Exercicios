# programa que ler o ano de nascimento e infoma se está com idade de se alistar 
from datetime import date
ano_usuario = int(input('Qual a sua data de nascimento? '))
data_atual = date.today()
idade_usuario = data_atual - ano_usuario
print(idade_usuario) 
# se ele ainda vai se alistar no serviço militar
# se é a hora de se alistar
# ja passou da hora de se alistar 
# mostrar o tempo que ainda falta e o ano que passou para se alistar