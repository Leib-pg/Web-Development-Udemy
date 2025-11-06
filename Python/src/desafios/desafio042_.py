from datetime import date

anoDeNascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoDeNascimento

if idade == 18:
    print('Você está na idade de se alistar.')
elif idade > 18:
    passou = idade - 18
    ano_alistamento = anoAtual - passou
    print(f'A idade de se alistar já passou há {passou} ano(s).')
    print(f'Você deveria ter se alistado em {ano_alistamento}.')
else:
    falta = 18 - idade
    ano_alistamento = anoAtual + falta
    print(f'Calma rapaz, ainda falta {falta} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {ano_alistamento}.')
