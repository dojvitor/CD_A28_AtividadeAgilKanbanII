def media(lista):
    medias = []
    for nome, notas in lista:
        media = sum(notas) / len(notas)
        medias.append((nome, media))
    return medias