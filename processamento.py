def media(lista):
    medias = []
    for nome, notas in lista:
        media = sum(notas) / len(notas)
        medias.append((nome, media))
    return medias
def varredura (lista):
    print(f"Lista atual: {lista}")
    for n in lista:
        if '' in n:
            print(f"Informação corrompida ou vazia encontrada em {n}!\nApagando item da lista...")
            lista.remove(n)
        print(f"Veja a nova lista após a varredura: \n {lista}")
    return lista
