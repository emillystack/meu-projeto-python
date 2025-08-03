# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
n=input('Olá aluno! Qual é o seu nome?')
p1=float(input('Certo, {}. Qual foi a sua nota na primeira prova?'.format(n)))
p2=float(input('Qual foi a sua nota na segunda prova?'))
m=(p1+p2)/2
print('Entendi! Então, {}. Analisando suas notas {} e {} \nA média das suas provas é de {:.1f}'.format(n,p1,p2,m))
# O ":.1f" arrendondou a nota média das provas
