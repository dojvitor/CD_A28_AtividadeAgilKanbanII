def media(lista):
    medias = []
    for nome, notas in lista:
        media = sum(notas) / len(notas)
        medias.append((nome, media))
    return medias

def filtro(lista):
    aprovados = []
    reprovados = []
    maior_media = max(media for nome, media in lista)
    for nome, media in lista:
        if media >= 70:
            aprovados.append(nome)
        else:
            reprovados.append(nome)
    
        if media == maior_media:
            top_student = nome
            print(f"Aluno {nome} é o Top Student!")
    return aprovados, reprovados, top_student
def varredura (lista):
    print(f"Lista atual: {lista}")
    for n in lista:
        if '' in n:
            print(f"Informação corrompida ou vazia encontrada em {n}!\nApagando item da lista...")
            lista.remove(n)
        print(f"Veja a nova lista após a varredura: \n {lista}")
    return lista
