# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (US1,00=R$5,76)
real=float(input('Quantos reais você tem disponível para gastar hoje? R$'))
dolar=real/5.76
print('Com R${:.2f} você conseguirá comprar {:.2f} dólares.'.format(real,dolar))
