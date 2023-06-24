"""
Implementing key indexed counting to use in Radix sorts

We have an array whose entries are between 0 and R - 1

We maintain a count array of size R
"""

def index_sort(v, R=100):
    n, c = len(v), 0
    if n < 3 * R: v.sort(); return
    counts = [0 for _ in range(R)]
    for i in range(n):
        counts[v[i]] += 1
    for r, count in enumerate(counts):
        for k in range(count):
            v[c] = r; c += 1
            if c >= n: return

if __name__ == '__main__':
    v = [1, 4, 8, 9, 3, 2, 7, 6, 5, 8, 7, 5]
    index_sort(v, R=10)
    print(v)



