# Peça um número inteiro ao usuário e exiba a tabuada desse número de 1 a 10.

numero=int(input("Digite um número inteiro: "))

i=1

while True:

    print(f"O resultado de {numero} * {i} = {numero*i}")

    i=i+1

    if(i>10):
        break

