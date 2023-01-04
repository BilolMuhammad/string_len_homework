def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    if len(s) % 2 == 0:
        return len(s)//2


print(main('fsdfsfkjgh'))
