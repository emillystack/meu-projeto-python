# Escreva um programa que leia o valor em metros e exiba convertido em centímetros e milímetros
m=float(input('Digite um distância em metros?'))
print('Com base na distancia de {} metros \nÉ o mesmo que {:.0f}cm \nE o mesmo que {:.0f}mm'.format (m,m*100,m*1000))
