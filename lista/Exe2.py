# Faça um programa que solicite números ao usuário até que ele digite um número negativo.
# Quando isso acontecer, o programa deve exibir a soma de todos os números positivos
# digitados e encerrar.

soma = 0

while True:
    numero=int(input("Digite um número(Digite um número negativo para encerrar: "))

    if(numero<0):
        break
    soma+=numero        

print(f"A soma dos números positivos é {soma}")
