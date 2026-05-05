with open("notas.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteudo guardado no arquivo:")
    print(conteudo)