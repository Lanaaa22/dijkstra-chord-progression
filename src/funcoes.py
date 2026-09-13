def entrada_acordes(qtd):
    l = []
    for i in qtd:
        acorde = int(input(f"Digite o {i+1} acorde: "))
        l.append(acorde)
    return l 