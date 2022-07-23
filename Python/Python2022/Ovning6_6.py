antal = int(input('Antal: '))

matris = []
for i in range(1, antal + 1):
    vektor = []
    for j in range(1, antal + 1):
        tal = int(input(f'Tal [{i}, {j}]: '))
        vektor.append(tal)
    matris.append(vektor)
print(matris)

# 1 2 3
# 2 1 3
# 3 3 1

symmetrisk = True
for i in range(0, antal):
    vecktor = []
    for j in range(0, antal):
        if matris[i][j] != matris[j][i]:
            symmetrisk = False
            break
    if not symmetrisk:
        break

print(f'{"Symmetrisk" if symmetrisk else "Ej symmetrisk"}')
