while True:
    try:
        produto = float(input('Qual o valor do produto? '))
        desconto = produto - (produto * 12/100) #formula do desconto
    except ValueError:
        print('Apenas valores númericos são aceitos...')
    else:
        print(f'O produto com 12% de desnconto sairá por {desconto}')   
        break
