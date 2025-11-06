numeroPar = 0
nuemroU = 0
for i in range(1,7):
  numeroU = int(input('Digite numeros: '))
  if numeroU % 2 == 0:
    numeroPar += 1
  print(f'A quantidade de numeros pares é {numeroPar}')
