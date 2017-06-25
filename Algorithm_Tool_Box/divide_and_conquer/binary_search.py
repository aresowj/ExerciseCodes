# Uses python3
import sys


def _binary_search(a, x, start, end):
    """Start and end positions are inclusive"""
    if start < end:
        length = end - start
        mid = start + int(length / 2) if length % 2 else start + int((length + 1 ) /2)
        # print('\n', start, end, mid, '\n')
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            return _binary_search(a, x, start, mid-1)
        elif x > a[mid]:
            return _binary_search(a, x, mid+1, end)
    elif start == end and start < len(a) and a[start] == x:
        return start
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    a_length = len(a)
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(_binary_search(a, x, 0, a_length), end = ' ')
