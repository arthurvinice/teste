#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibo(x):
    fib_seq = [0, 1]
    while fib_seq[-1] < x:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if x in fib_seq:
        return True
    else:
        return False
    
def main():
    x = int(input("digite um número: "))
    if fibo(x):
        print(f"{x} pertence à sequência de Fibonacci.")
    else:
        print(f"{x} não pertence à sequência de Fibonacci.")

main()
