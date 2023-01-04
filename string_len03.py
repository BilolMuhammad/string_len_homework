def main(a, b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    l1 = len(a)
    l2 = len(b)
    return l1 == l2


print(main('asd', 'asd'))
print(main('1sd', 'dssasd'))
