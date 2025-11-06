#Ultilizando laço while basico
sair = ''
while sair != 'S' and sair != 'SIM':
    num1 = int(input('Digite um número para somar: '))
    num2 = int(input('Digite outro número: '))
    print(f'A soma é {num1 + num2}')
    sair = input('Você quer sair? [S/N]: ').strip().upper()
