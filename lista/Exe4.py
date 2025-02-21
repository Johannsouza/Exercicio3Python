# Peça ao usuário dois números inteiros, representando um intervalo A,B. O programa deve
# exibir todos os números ímpares dentro desse intervalo (inclusive os limites, se forem
# ímpares).

a=int(input("Digite um número inteiro: "))
b=int(input("Digite outro número inteiro: "))

if a > b:
    a, b = b,a  

for i in range(a, b + 1):  
    if i % 2 != 0:  
        print(i)
