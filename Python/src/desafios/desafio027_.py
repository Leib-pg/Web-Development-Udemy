import random
while True:
  numero_do_robo = random.randint(0, 5)
  numero_do_usuario = int(input('Tende adivinhar o numero escolhido: '))
  if numero_do_usuario == numero_do_robo:
    print('voce acertou')
    break
  else:
    print(f'você errou o numero certo seria: {numero_do_robo} ')
    break
