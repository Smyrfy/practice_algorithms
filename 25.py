def climb_recursive(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    return climb_recursive(n - 1) + climb_recursive(n - 2)