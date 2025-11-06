
numeroPar = 0
numeroImp = 0
for i in range(1,501):
  if i % 2 == 0:
    numeroPar += 1
  else:
    numeroImp += 1

print(f'quantidade de pares = {numeroPar}')
print(f'quantidade de impares = {numeroImp}')

