# programa que o pc recee um numero aleatorio de 1 a 10 e o usuario tenta adivinhar
import random
jogador = 0
computador = random.randint(1, 10)
while jogador != computador:
  jogador = int(input("Digite um número entre 1 e 10: "))
  if jogador == computador:
      print("Parabéns! Você acertou de primeira!")
  else:
      print("Tente novamente.")
