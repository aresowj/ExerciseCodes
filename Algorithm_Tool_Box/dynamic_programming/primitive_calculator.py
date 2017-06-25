# Uses python3
import sys

# The cache stores for the number n (key), the next value
# that could reach to the min operations until 1.
cache_next = {2: 1, 3: 2}
cache_counts = {1: 0, 2: 1, 3: 1}


def min_operations(x):
    global cache_counts, cache_next

    if x == 1:
        return 0
    if x == 2 or x == 3:
        return 1

    if x in cache_counts:
        # Use cached counts if exists
        return cache_counts[x]

    min_1 = min_operations(x-1)
    min_2 = float('inf')
    min_3 = float('inf')
    min_all = float('inf')

    if x % 3 == 0:
        min_3 = min_operations(x/3)        
    if x % 2 == 0:
        min_2 = min_operations(x/2)
    
    min_all = min(min_3, min_2, min_1)
    cache_counts[x] = min_all + 1
    
    if min_all == min_3:
        cache_next[x] = int(x / 3)
    elif min_all == min_2:
        cache_next[x] = int(x / 2)
    else:
        cache_next[x] = x - 1

    return cache_counts[x]


def optimal_sequence(n):
    seq = []
    i = 4
    while i <= n:
        min_operations(i)
        i += 1
        
    print(cache_counts[n])
    while True:
        seq.append(n)
        if n > 1:
            n = cache_next[n]
        else:
            break
    for num in reversed(seq):
        print(num, end=' ')

input = sys.stdin.read()
n = int(input)
optimal_sequence(n)

