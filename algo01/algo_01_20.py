# https://skillsmart.ru/algo/lvl1/o83c.html

# string [] TreeOfLife(int H, int W, int N, string [] tree)

def TreeOfLife(H, W, N, tree):
    year = 1
    tree = build_tree(tree)
    
    while year < N + 1:
        year += 1
        inc_tree(tree)
        if year % 2 != 0:
            rebuild_tree(H, W, tree)
    
    return export_tree(tree)


def export_tree(tree_in):
    result = []
    for row in tree_in:
        r = []
        for cell in row:
            if cell > 0:
                r.append('+')
            else:
                r.append('.')
        result.append(''.join(r))
    return result
    

def rebuild_tree(H, W, tree_in):
    for ix in range(H):
        for iy in range(W):
            cell = tree_in[ix][iy]
            if cell < 3:
                continue
            else:
                tree_in[ix][iy] = -1
                if iy - 1 >= 0:
                    if tree_in[ix][iy - 1] < 3:
                        tree_in[ix][iy - 1] = -1
                if iy + 1 < W:
                    if tree_in[ix][iy + 1] < 3:
                        tree_in[ix][iy + 1] = -1
                if ix - 1 >= 0:
                    if tree_in[ix - 1][iy] < 3:
                        tree_in[ix - 1][iy] = -1
                if ix + 1 < H:
                    if tree_in[ix + 1][iy] < 3:
                        tree_in[ix + 1][iy] = -1
    for row in tree_in:
        for (ix, cell) in enumerate(row):
            if row[ix] == -1:
                row[ix] += 1


def inc_tree(tree_in):
    for row in tree_in:
        for (ix, cell) in enumerate(row):
            row[ix] += 1


def build_tree(tree_in):
    tree = []
    for row in tree_in:
        r = []
        for cell in row:
            if cell == '.':
                r.append(0)
            else:
                r.append(1)
        tree.append(r)
    return tree
