#Uses python3
import sys
import math
import random


def partition3(x, y, l, r):
    pivot = x[l]
    j = l
    k = l
    i = l + 1
    while i <= r:
        if x[i] < pivot:
            j += 1
            x[i], x[j] = x[j], x[i]
            y[i], y[j] = y[j], y[i]
            if j > k:
                k = j
        elif x[i] == pivot:
            k += 1
            x[i], x[k] = x[k], x[i]
            y[i], y[k] = y[k], y[i]

        i += 1
    x[l], x[j] = x[j], x[l]
    y[l], y[j] = y[j], y[l]
    return j, k


def randomized_quick_sort(x, y, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    x[l], x[k] = x[k], x[l]
    y[l], y[k] = y[k], y[l]
    #use partition3
    m, n = partition3(x, y, l, r)
    randomized_quick_sort(x, y, l, m - 1)
    randomized_quick_sort(x, y, n + 1, r)


def dist(x, y, i, j):
    return math.sqrt((x[j]-x[i])**2 + (y[j]-y[i])**2)


def search_min(x, y, start, end):
    min_dist = float('inf')
    for i in range(start, end):
        for j in range(start, end):
            dist = dist(x, y, i, j)
            if dist < min_dist:
                min_dist = dist


def minimum_distance(x, y, start, end):
    if end == start:
        return None
    elif end - start == 1:
        return dist(x1, y1, x2, y2)

    mid = len(x) / 2 if len(x) % 2 else (len(x) + 1) / 2
    min_dist_left = search_min(x, y, start, mid-1)
    mindist_right = search_min(x, y, mid, end)

    if dist_left is None and dist_right is None:
        return None

    return min(dist_left or dist_right, dist_right or dist_left)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    randomized_quick_sort(x, y, 0, len(x)-1)
    print("{0:.9f}".format(minimum_distance(x, y, 0, n)))
