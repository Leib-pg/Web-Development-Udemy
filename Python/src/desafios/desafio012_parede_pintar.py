# lendo altura e largura de uma parede em metros e calculando sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
aT = l * a
print('a área de sua parede é {}'.format(aT))
qt = aT / 2
print('para pinta sua parede você vai precisar {}l de tinta'.format(qt))
