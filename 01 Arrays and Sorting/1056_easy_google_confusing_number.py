"""

"""

def confusing(n):
    confused, ns = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}, str(n)

    def rotate(ns):
        s = ''
        for c in ns:
            if c not in confused: return None
            s += confused[c]
        return s[::-1]

    rs = rotate(ns)
    if not rs: return False
    return rs != ns