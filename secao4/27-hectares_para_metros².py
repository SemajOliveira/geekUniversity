while True:
    try:
        h = float(input('Digite os hectares: '))
        m = h * 10_000 #formula de conversão
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor lido: {h}')
        print(f'Valor convertido para metros quadrados: {m}')
        break
