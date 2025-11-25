import random

print("PIXVERSARIO, escolha um intervalo de dois numeros e sorteie seu pix ! ")
PrimeiroNumero = input("Digite o valor mínimo (apenas números inteiros) : ")
UltimoNumero = input("Digite o valor máximo (apenas números inteiros) : ")

PrimeiroNumero = (int(PrimeiroNumero))
UltimoNumero = (int(UltimoNumero))

Random = random.randint(PrimeiroNumero, UltimoNumero)

print("Faca seu PIX de : R$", Random,"00")
