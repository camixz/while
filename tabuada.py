#Tabuada
número = int(input('Digite um número:'))

multiplicador = 1

while(multiplicador <=10):
    resultado = número * multiplicador
    print(f'{número} x {multiplicador} = {resultado}')
    multiplicador = multiplicador + 1