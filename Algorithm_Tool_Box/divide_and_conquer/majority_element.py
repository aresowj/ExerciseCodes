# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    a.sort()

    count = 1
    for i in range(len(a)):
        if i < len(a) - 1:
            if a[i] == a[i+1]:
                count += 1
            else:
                count = 1

        if count > len(a)/2:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
