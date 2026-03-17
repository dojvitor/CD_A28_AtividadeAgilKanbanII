def varredura (lista):
    print(f"Lista atual: {lista}")
    for n in lista:
        if '' in n:
            print(f"Informação corrompida ou vazia encontrada em {n}!\nApagando item da lista...")
            lista.remove(n)
        print(f"Veja a nova lista após a varredura: \n {lista}")
    return lista