def find_product(products: list, target: str) -> int:
    for i in range(len(products)):
        if products[i] == target:
            return i + 1   # індексація з 1
    return -1
