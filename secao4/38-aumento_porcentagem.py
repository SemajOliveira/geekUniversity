while True:
    try:
        salario = float(input('Digite seu salário R$: '))
        aumento =  salario + (salario * 25/100) # formula do aumento
    except ValueError:
        print('Apenas valores númericos são aceitos...')
    else:
        print(f'Com 25% de aumento seu novo salário será de R${aumento}')  
        break
