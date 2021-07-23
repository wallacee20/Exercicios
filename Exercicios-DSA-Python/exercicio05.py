# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
 
''' 
***** CORREÇÂO *****

temperatura = 40  
while temperatura > 35: 
    print(temperatura)
    temperatura = temperatura - 1
40
39
38
37
36
**********************'''
    
temperatura = float(input('Digite a temperatura do dia!: '))

if temperatura > 35 :
    print(f'{temperatura}°C, Temperatura insuportável!')

elif temperatura > 27 and temperatura < 35:
    print(f'{temperatura}°C, Temperatura Quente!')

elif temperatura < 27 and temperatura > 15:
    print(f'{temperatura}°C, Temperatura Agradavel')

elif temperatura < 15 and temperatura > 10:
    print(f'{temperatura}°C, Temperatura Esfrio Bastante')

else:
    print(f'{temperatura}°C, A temperatura está muito Frio')