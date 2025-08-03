# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
print('O nosso mercadinho está com promoção! \nTodos os produtos com 5% de desconto!')
print('-'*20)#Pra embelezar
print(' ')
p=float(input('Vou mostrar quanto ele vai custar com o desconto! \nDigite o valor: R$'))
d=p*5/100 #Para calcular o desconto de 5%, multiplique o valor do produto por 5 e divida por 100
r=p-d
print('Considerando o valor do produto de R${:.2f}\nEle fica desconto de R${:.2f} \nAgora ele está pelo valor de R${:.2f}!'.format(p,d,r))
