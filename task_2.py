class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min_value(node):
    if node is None:
        return None

    current = node
    while current.left is not None:
        current = current.left

    return current.key

# Приклад використання:
if __name__ == "__main__":
    # Створимо дерево:
    #      20
    #     /  \
    #    10   30
    #   /  \
    #  5    15

    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)

    min_val = find_min_value(root)
    print(f"Найменше значення у дереві: {min_val}")  # Очікуваний результат: 5
