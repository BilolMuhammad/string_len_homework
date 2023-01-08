def main(s1, s2, s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". 
    If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    sum = ''
    if len(s1) % 2 != 0:
        sum += s1
    if len(s2) % 2 != 0:
        sum += s2
    if len(s3) % 2 != 0:
        sum += s3
    if len(sum) != 0:
        return f'[{sum}]'
    else:
        return f'[]'


print(main('ssd', 'sdf', '^fds'))
print(main('ssd', 'sdf3', 'ss'))
print(main('ssdx', 'csdf', 'v^fdss'))
