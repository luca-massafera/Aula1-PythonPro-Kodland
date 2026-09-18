import random

caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

comprimento = input("Digite o comprimento da senha: ")

senha = ""

for i in range(int(comprimento)):
    senha += random.choice(caracter)

print("Senha gerada:", senha)
