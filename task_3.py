class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def calculate_tree_sum(node):
    if node is None:
        return 0

    return node.key + calculate_tree_sum(node.left) + calculate_tree_sum(node.right)

# Приклад використання:
if __name__ == "__main__":
    # Створимо дерево:
    #        50
    #      /    \
    #    30      70
    #   /  \    /  \
    #  20  40  60  80

    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    total_sum = calculate_tree_sum(root)
    print(f"Сума всіх значень у дереві: {total_sum}")
