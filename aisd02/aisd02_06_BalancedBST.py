class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        a_ = a.copy()
        a_.sort()

        def fillTree(parent, nodes, lvl):
            if len(nodes) == 0:
                return

            node = BSTNode(nodes[len(nodes) // 2], parent)
            node.Level = lvl

            if parent is None:
                self.Root = node
            else:
                if parent.LeftChild is None:
                    parent.LeftChild = node
                else:
                    parent.RightChild = node

            fillTree(node, nodes[:len(nodes) // 2], lvl + 1)
            fillTree(node, nodes[len(nodes) // 2 + 1:], lvl + 1)

        fillTree(None, a_, 0)

    def IsBalanced(self, root_node):
        if root_node is None:
            return True
        minNode = self.FinMinMax(root_node.LeftChild, False)
        maxNode = self.FinMinMax(root_node.RightChild, True)
        return abs(minNode.Level - maxNode.Level) < 2

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальное/минимальное (узел) в поддереве
        node = FromNode if FromNode is not None else self.Root
        if node is None:
            return None
        child = node.RightChild if FindMax else node.LeftChild
        if child is None:
            return node
        return self.FinMinMax(child, FindMax)
