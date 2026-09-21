from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    result = [[rStart, cStart]]
    r, c = rStart, cStart
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    steps = 1

    while len(result) < rows * cols:
        for _ in range(2):
            dr, dc = directions[direction]

            for _ in range(steps):
                r += dr
                c += dc

                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])

                    if len(result) == rows * cols:
                        return result

            direction = (direction + 1) % 4

        steps += 1

    return result


if __name__ == '__main__':
    rows, cols, rStart, cStart = map(int, input().split())
    print(spiralMatrixIII(rows, cols, rStart, cStart))