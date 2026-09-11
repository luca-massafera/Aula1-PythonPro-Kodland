meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "Abreviação da palavra 'verdade'",
            "BISCOITAR": "Postar algo apenas para chamar atenção",
            "HATER": "Pessoa que está constantemente criticando os outros",
            "VLW": "Abreviação da palavra 'valeu'"
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

print("")

if word in meme_dict.keys():
    # O que devemos fazer se a palavra for encontrada?
    print("A palavra", word, "significa:")
    print("")
    print(meme_dict[word])
else:
    # O que devemos fazer se a palavra não for encontrada?
    print("Infelizmente a palavra não foi encontrada")
