# Escreva um programa que peça ao usuário um número N e exiba os N primeiros termos da
# Sequência de Fibonacci.
# Obs: A sequência de Fibonacci começa com 0 e 1, e cada termo seguinte é a soma dos dois
# anteriores:

N = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

if N <= 0:
    print("Por favor, digite um número maior que zero.")
else:
    
    fib1, fib2 = 0, 1

    print("Sequência de Fibonacci:")
    for i in range(N):
        print(fib1, end=" ")  
        fib1, fib2 = fib2, fib1 + fib2 
