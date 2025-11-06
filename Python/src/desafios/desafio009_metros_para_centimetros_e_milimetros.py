# programa que lê um valor em metros e o exibe convertido em centímetros e milímetros

valor_metros = float(input('Digite um valor em metros: '))
valor_centimetros = valor_metros * 100
valor_milimetros = valor_metros * 1000
print('{} metros equivalem a {} centímetros e {} milímetros.'.format(valor_metros, valor_centimetros, valor_milimetros))
