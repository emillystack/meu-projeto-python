# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n=int(input('Digite um número:'))
d=n*2
t=n*3
q=n**(1/2) #precisamos colocar parenteses no 1/2 pra calcular primeiro e depois fazer a pontência. ORDEM DE PRECEDENCIA
print('Analisando o número {} \nSeu dobro é {} \nSeu triplo é {} \nSua raiz quadrada é {:.2f}'.format(n,d,t,q))
