import funcoes as f
def main():
    #entrada de dados
    print("==== BEM VINDO ===")
    quantidade_acordes = int(input("Quantidade de Acordes: "))
    acordes = f.entrada_acordes(quantidade_acordes)
    print(acordes) 