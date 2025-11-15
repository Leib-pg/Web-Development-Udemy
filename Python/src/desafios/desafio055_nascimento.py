# colocando quantos tem maior de idade e quantos não

maior = 0
menor = 0
for i in range(1, 8):
  anoDeNascimento = int(input('Digite o seu ano de nascimento: '))
  idade = 2025 - anoDeNascimento
  if idade >= 18:
    maior += 1
  else:
    menor += 1

print(f'Temos {maior} pessoas maiores de idade.')
print(f'Temos {menor} pessoas menores de idade.')
