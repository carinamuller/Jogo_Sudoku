tabuleiro = [
    [1, 0, 3, 0],
    [0, 4, 0, 2],
    [2, 0, 4, 0],
    [0, 3, 0, 1]
]

def mostrar(tabu):
    for linha in tabu:
        print(*("." if v == 0 else v for v in linha))
    print()

def valido(tabu, l, c, v):
    for i in range(4):
        if tabu[l][i] == v or tabu[i][c] == v:
            return False
    il, ic = (l // 2) * 2, (c // 2) * 2
    for i in range(2):
        for j in range(2):
            if tabu[il + i][ic + j] == v:
                return False
    return True

def completo(tabu):
    for linha in tabu:
        if 0 in linha:
            return False
    return True

print("Bem-vindo ao Sudoku 4x4!")
mostrar(tabuleiro)

while not completo(tabuleiro):
    try:
        l = int(input("Linha (0-3): "))
        c = int(input("Coluna (0-3): "))
        v = int(input("Valor (1-4): "))

        if tabuleiro[l][c] != 0:
            print("Essa posição já está preenchida!")
            continue

        if valido(tabuleiro, l, c, v):
            tabuleiro[l][c] = v
            mostrar(tabuleiro)
        else:
            print("Jogada inválida! \n")

    except Exception as e:
        print("Entrada inválida.\n")

print("Parabéns, você venceu!")
mostrar(tabuleiro)


