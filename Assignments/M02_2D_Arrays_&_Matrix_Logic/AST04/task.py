def diagonalSort(mat):
    m = len(mat)
    n = len(mat[0])

    for start in range(m):
        diagonal = []
        i, j = start, 0

        while i < m and j < n:
            diagonal.append(mat[i][j])
            i += 1
            j += 1

        diagonal.sort()

        i, j = start, 0
        k = 0

        while i < m and j < n:
            mat[i][j] = diagonal[k]
            i += 1
            j += 1
            k += 1

    for start in range(1, n):
        diagonal = []
        i, j = 0, start

        while i < m and j < n:
            diagonal.append(mat[i][j])
            i += 1
            j += 1

        diagonal.sort()

        i, j = 0, start
        k = 0

        while i < m and j < n:
            mat[i][j] = diagonal[k]
            i += 1
            j += 1
            k += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = []

    for i in range(m):
        mat.append(list(map(int, input().split())))

    print(diagonalSort(mat))