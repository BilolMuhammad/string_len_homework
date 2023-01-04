def main(num1, num2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    num1 = int(num1)
    num2 = int(num2)
    if num1 > 0 and num2 > 0:
        return f"'{str(num1+num2)}'"
    else:
        return 'Please,enter non-negative integers,represented as string'


print(main('72', '54'))
