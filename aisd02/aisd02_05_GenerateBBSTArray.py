def GenerateBBSTArray(a):
    """
    Возвращает сбалансированное BST дерево.

    Parameters:
        a (list): неотсортированный массив размера заполненого дерева некоторой глубины H > 0
    Returns:
        list: массив, содержащий структуру сбалансированного BST
    """

    a_ = a.copy()
    a_.sort()

    depth = 0
    while True:
        depth += 1
        tree_size = 2 ** depth - 1
        if tree_size >= len(a):
            break

    bbst = [None] * tree_size

    def fillTree(ix, nodes):
        if len(nodes) == 0:
            return
        bbst[ix] = nodes[len(nodes) // 2]
        fillTree(2 * ix + 1, nodes[:len(nodes) // 2])
        fillTree(2 * ix + 2, nodes[len(nodes) // 2 + 1:])

    fillTree(0, a_)
    return bbst
