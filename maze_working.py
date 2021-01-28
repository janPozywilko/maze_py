from random import shuffle, randrange


def make_maze(w=16, h=8):
    visited = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    vertical = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    horizontal = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        visited[y][x] = 1

        direction = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(direction)
        for (xx, yy) in direction:
            if visited[yy][xx]: continue
            if xx == x: horizontal[max(y, yy)][x] = "+  "
            if yy == y: vertical[y][max(x, xx)] = "   "
            walk(xx, yy)
            print(horizontal[0,0])


    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(horizontal, vertical):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s



if __name__ == '__main__':

    result = make_maze()
    print(result)
    # for item in range(int(len(result))):
    #     print(result[item])
