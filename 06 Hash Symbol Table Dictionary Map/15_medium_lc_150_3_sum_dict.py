"""

"""

from collections import defaultdict

def map_vec(vec):
    dic = defaultdict(list)
    for i, v in enumerate(vec):
        if len(dic[v]) < 3:
            dic[v].append(i)
    return dic

def three_sum(ns):
    result = set()
    if not ns: return result
    dic, n = map_vec(ns), len(ns)
    if len(dic) == 1: return [[0, 0, 0]] if ns[0] == 0 else []
    for i in range(n):
        for j in range(i + 1, n):
            nij = -(ns[i] + ns[j])
            ks = dic[nij]
            for k in ks:
                if k != i and k != j:
                    result.add(tuple(sorted([ns[i], ns[j], ns[k]])))
    return result

