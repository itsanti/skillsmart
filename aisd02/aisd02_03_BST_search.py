class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def __str__(self):
        return '(' + str(self.NodeKey) + ')'


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def __str__(self):
        return str(self.Root)

    def FindNodeByKey(self, key):
        result = BSTFind()
        node: BSTNode = self.Root
        while node is not None:
            if node.NodeKey == key:
                result.Node = node
                result.NodeHasKey = True
                return result
            elif node.NodeKey > key:
                result.ToLeft = True
                if node.LeftChild is None:
                    result.Node = node
                    return result
                else:
                    node = node.LeftChild
            elif node.NodeKey < key:
                result.ToLeft = False
                if node.RightChild is None:
                    result.Node = node
                    return result
                else:
                    node = node.RightChild
        return result

    def AddKeyValue(self, key, val):
        bst_find = self.FindNodeByKey(key)
        if bst_find.NodeHasKey:
            return False
        parent = bst_find.Node
        node = BSTNode(key, val, parent)
        if parent is None:
            self.Root = node
        else:
            if bst_find.ToLeft:
                parent.LeftChild = node
            else:
                parent.RightChild = node
        return True

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальное/минимальное (узел) в поддереве
        node = FromNode if FromNode is not None else self.Root
        if node is None:
            return None
        child = node.RightChild if FindMax else node.LeftChild
        if child is None:
            return node
        return self.FinMinMax(child, FindMax)

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        bst_find = self.FindNodeByKey(key)
        if not bst_find.NodeHasKey:
            return False  # если узел не найден

        node = bst_find.Node

        if node.LeftChild is not None and node.RightChild is not None:
            min_node = self.FinMinMax(node.RightChild, FindMax=False)

            if min_node.LeftChild is None and min_node.RightChild is None:
                self.DeleteNodeByKey(min_node.NodeKey)
                min_node.LeftChild = node.LeftChild
                node.LeftChild.Parent = min_node
                min_node.RightChild = node.RightChild
                node.RightChild.Parent = min_node
                min_node.Parent = node.Parent
                if bst_find.ToLeft:
                    node.Parent.LeftChild = min_node
                else:
                    node.Parent.RightChild = min_node
                node.Parent = None
            else:
                if min_node.Parent is node:
                    min_node.LeftChild = node.LeftChild
                    node.LeftChild.Parent = min_node
                    min_node.Parent = node.Parent
                    if bst_find.ToLeft:
                        node.Parent.LeftChild = min_node
                    else:
                        node.Parent.RightChild = min_node
                    node.Parent = None
                else:
                    min_node.RightChild.Parent = min_node.Parent
                    min_node.Parent.LeftChild = min_node.RightChild

                    min_node.Parent = node.Parent
                    node.Parent = None

                    min_node.LeftChild = node.LeftChild
                    node.LeftChild.Parent = min_node
                    min_node.RightChild = node.RightChild
                    node.RightChild.Parent = min_node

                    if bst_find.ToLeft:
                        min_node.Parent.LeftChild = min_node
                    else:
                        min_node.Parent.RightChild = min_node

        else:
            if node.LeftChild is None and node.RightChild is None:
                if node.Parent is None:
                    self.Root = None
                else:
                    if bst_find.ToLeft:
                        node.Parent.LeftChild = None
                    else:
                        node.Parent.RightChild = None
                    node.Parent = None
            else:
                child = node.LeftChild if node.LeftChild is not None else node.RightChild

                if bst_find.ToLeft:
                    node.Parent.LeftChild = child
                else:
                    node.Parent.RightChild = child

                child.Parent = node.Parent

        node.LeftChild = None
        node.RightChild = None

        return True

    @staticmethod
    def subnodes(acc, node):
        if node is None:
            return
        acc[0] += 1
        if node.LeftChild is not None:
            BST.subnodes(acc, node.LeftChild)
        if node.RightChild is not None:
            BST.subnodes(acc, node.RightChild)

    def Count(self):
        if self.Root is None:
            return 0
        acc = [0]
        BST.subnodes(acc, self.Root)
        return acc[0]

    def WideAllNodes(self):
        if self.Root is None:
            return []
        result = [self.Root]
        check = [self.Root]
        while len(check) > 0:
            node = check.pop(0)
            if node.LeftChild is not None:
                check.append(node.LeftChild)
                result.append(node.LeftChild)
            if node.RightChild is not None:
                check.append(node.RightChild)
                result.append(node.RightChild)
        return result

    def DeepAllNodes(self, order):
        def deep(node):
            if node is None:
                return []
            result = []
            if order == 2:  # pre-order
                result.append(node)
            result.extend(deep(node.LeftChild))
            if order == 0:  # in-order
                result.append(node)
            result.extend(deep(node.RightChild))
            if order == 1:  # post-order
                result.append(node)
            return result
        return deep(self.Root)
