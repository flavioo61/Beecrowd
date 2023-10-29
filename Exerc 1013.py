# Exerc 1013 - O Maior
# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
# MaiorAB = (a+b+abs(a-b))/2
# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.
# Entrada
# O arquivo de entrada contém três valores inteiros.
# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

# Resposta

A, B, C = map(int, input().split())

maiorAB = (A+B+abs(A-B))/2
maiorValor = (maiorAB + C+abs(maiorAB-C))/2
print(f'{int(maiorValor)} eh o maior')
