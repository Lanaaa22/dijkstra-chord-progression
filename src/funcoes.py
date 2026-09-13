notas = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}

# Entrada dos acordes
def entrada_acordes(qtd):
    l = []
    for i in range(qtd):
        acorde = input(f"Digite o {i+1} acorde: ").upper()
        while acorde not in ["C", "Cm", "C#", "D", "Dm", "D#", "E", "Em", "F", "Fm", "F#", "G", "Gm", "G#", "A", "Am", "A#", "B"]:
            print("Essa letra não é um acorde!. Tente novamente abaixo")
            acorde = input(f"Digite o {i+1} acorde: ").upper()
        l.append(acorde)
    return l 

def calcula_semitons(t1, t2):
    return (notas[t1] - notas[t2]) % 12

def encontra_tonica(acorde, estado):
    acordes_composição = {
    'C':  ['C', 'E', 'G'],
    'Cm': ['C', 'D#', 'G'],
    'C#': ['C#', 'F', 'G#'],
    'D':  ['D', 'F#', 'A'],
    'Dm': ['D', 'F', 'A'],
    'D#': ['D#', 'G', 'A#'],
    'E':  ['E', 'G#', 'B'],
    'Em': ['E', 'G', 'B'],
    'F':  ['F', 'A', 'C'],
    'Fm': ['F', 'G#', 'C'],
    'F#': ['F#', 'A#', 'C#'],
    'G':  ['G', 'B', 'D'],
    'Gm': ['G', 'A#', 'D'],
    'G#': ['G#', 'C', 'D#'],
    'A':  ['A', 'C#', 'E'],
    'Am': ['A', 'C', 'E'],
    'A#': ['A#', 'D', 'F'],
    'B':  ['B', 'D#', 'F#']}
    nota_acorde = acordes_composição[acorde]
    baixo = nota_acorde[estado - 1] #1, 2, 3
    return notas[baixo]
    


