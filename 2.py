# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre
# será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule
# a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não
#  a sequência.


def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    if b == n or a == n:
        return True
    return False


n = int(input("Digite um número: "))

if fibonacci(n):
    print(f"{n} pertence à sequência de Fibonacci.")
else:
    print(f"{n} não pertence à sequência de Fibonacci.")
