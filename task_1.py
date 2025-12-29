class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max_value(node):
    if node is None:
        return None

    current = node
    while current.right is not None:
        current = current.right

    return current.key

# Приклад використання:
if __name__ == "__main__":
    # Створимо дерево:
    #      10
    #     /  \
    #    5    20
    #          \
    #           30

    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.right = Node(30)

    print(f"Найбільше значення у дереві: {find_max_value(root)}")
