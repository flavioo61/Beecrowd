# Exerc 1038 - Lanche
# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

#       | Codigo   | Especificação    | Preço |
#       |    1     |Cachorro Quente   |R$ 4.00|
#       |    2     |X-Salada          |R$ 4.50|
#       |    3     |X-Bacon           |R$ 5.00|
#       |    4     |Torrada simples   |R$ 2.00|
#       |    5     |Refrigerante      |R$ 1.50|
# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.
# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

# Resposta

codigo, quantidade = map(int, input().split())

precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

if codigo in precos:
    valor_total = precos[codigo] * quantidade
    print(f'Total: R$ {valor_total:.2f}')
else:
    print("Código de item inválido")