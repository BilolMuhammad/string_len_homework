def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    ans = ''

    jft1 = len(s)//2-1
    jft2 = len(s)//2
    if len(s) % 2 == 0:
        ans += s[jft1]
        ans += s[jft2]

    return ans


print(main('assf'))
