valor = 780_000

ganhador1 = valor * 0.46 # valor da porcentagem 46/100
ganhador2 = valor * 0.32 # valor da porcentagem 32/100
soma = ganhador1 + ganhador2 
ganhador3 = valor - soma # o ganhador 3 ganha a sobra

print(f'O ganhador 1 vai levar R$ {ganhador1}')
print(f'O ganhador 2 vai levar R$ {ganhador2}')
print(f'O ganhador 3 vai levar R$ {ganhador3}')
