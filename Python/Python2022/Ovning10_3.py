import math

def is_unique(list):
    return len(list) == len(set(list))

def Sudoku(matris):
    assert len(matris) == 9, ('Felaktig hojd', len(matris))
    for vektor in matris:
        assert len(vektor) == 9, ('Felaktig bredd', len(vektor))
        if not is_unique(vektor):
            return False

    for column in range(0, 9):
        vektor = []
        for rad in range(0, 9):
            vektor.append(matris[rad][column])
        if not is_unique(vektor):
            return False

    diagonal = []
    for index in range(0, 9):
        diagonal.append(matris[index][index])
    if not is_unique(diagonal):
        return False

    diagonal = []
    for index in range(0, 9):
        diagonal.append(matris[8 - index][index])
    if not is_unique(diagonal):
        return False

    region = matris[0][:3] + matris[1][:3] + matris[2][:3]
    if not is_unique(region):
        return False

    region = matris[0][3:6] + matris[1][3:6] + matris[2][3:6]
    if not is_unique(region):
        return False

    region = matris[0][6:] + matris[1][6:] + matris[2][6:]
    if not is_unique(region):
        return False

    region = matris[3][:3] + matris[4][:3] + matris[5][:3]
    if not is_unique(region):
        return False

    region = matris[3][3:6] + matris[4][3:6] + matris[5][3:6]
    if not is_unique(region):
        return False

    region = matris[3][6:] + matris[4][6:] + matris[5][6:]
    if not is_unique(region):
        return False

    region = matris[6][:3] + matris[7][:3] + matris[8][:3]
    if not is_unique(region):
        return False

    region = matris[6][3:6] + matris[7][3:6] + matris[8][3:6]
    if not is_unique(region):
        return False

    region = matris[6][6:] + matris[7][6:] + matris[8][6:]
    if not is_unique(region):
        return False

    return True

m = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9,],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]]

print(f'Sudoku: {Sudoku(m)}')

