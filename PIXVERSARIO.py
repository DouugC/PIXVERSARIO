import random

print("PIXVERSARIO, escolha um intervalo de dois numeros e sorteie seu pix ! ")
PrimeiroNumero = input("Digite o primeiro numero : ")
UltimoNumero = input("Digite o Ultimo numero : ")

PrimeiroNumero = (int(PrimeiroNumero))
UltimoNumero = (int(UltimoNumero))

Random = random.randint(PrimeiroNumero, UltimoNumero)

print("Faca seu PIX de : R$", Random,"00")
