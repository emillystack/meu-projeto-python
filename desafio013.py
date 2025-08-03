# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print(' ')
print('O salário aumentou 15%!')
print('.'*50)
s=float(input('Qual era o valor do seu antigo salário?R$'))
a=s*15/100
print('Considerando o seu salário de R${:.2f}'.format(s))
print('Com o aumento de 15% que fica +R${:.2f}'.format(a))
print('.'*50)
print('O seu salário será de R${:.2f} agora'.format(s+a))
