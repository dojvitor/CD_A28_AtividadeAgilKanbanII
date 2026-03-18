import processamento as process

lista_alunos = [("", [90.00, 71.00, 50.00, 45.00]), ("Vinícius", [100.00, 100.00, 99.00, 90.00, 25.00]), ("Vitor", [25.00, 25.00, 70.00, 10.00])]

process.varredura(lista_alunos)
resultado = process.media(lista_alunos)
print(resultado)
