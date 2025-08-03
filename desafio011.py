#Faça um programa que leia a largura e altura  de uma parede em metros, calcule a sua área e a quantidade de  tinta necessariária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²
print('Olá! Vamos calcular quanto de tinta você vai precisar para pintar sua parede!')
print('-'*30)#Só pra embelezar
print(' ')#Só pra embelezar
lar=float(input('Quantos metros a sua parede tem de largura?'))
alt=float(input('Quantos metros a sua parede tem de altura?'))
print(' ')#Só pra embelezar 
a=alt*lar
t=a/2
print('-'*30)#Só pra embelezar
print('Considerando a largura de {}m e altura de {}m \nA sua parede tem {}m² de área \nVocê vai precisar de {:.0f}l de tinta para pintar a sua parede.'.format(lar,alt,a,t))
