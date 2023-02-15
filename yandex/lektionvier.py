from itertools import chain


def sortscores(scores):
    mn, mx = min(scores), max(scores)
    c = [0] * (mx - mn + 1)

    for v in scores:
        c[v - mn] += 1

    res = []

    for i in range(len(c)):
        for j in range(c[i]):
            res.append(i + mn)
    return res


def checknumbers(a, b):
    def gnums(val):
        while val != 0:
            yield val % 10
            val //= 10

    return sortscores(list(gnums(a))) == sortscores(list(gnums(b)))


def checknumbers1(a, b):
    def cgnums(val):
        digits = [0] * 10

        while val != 0:
            digits[val % 10] += 1
            val //= 10
        return digits

    for a, b in zip(cgnums(a), cgnums(b)):
        if a != b:
            return False
    return True


def beatingrooks(coords):
    rows = {}
    cols = {}

    for row, col in coords:
        rows[row] = rows.setdefault(row, 0) + 1
        cols[col] = cols.setdefault(col, 0) + 1
    sm = 0
    for k, v in chain(rows.items(), cols.items()):
        sm += v - 1

    return sm


def hist(s):
    cnt = {}
    mxcnt = -1
    for c in s:
        cnt[c] = cnt.setdefault(c, 0) + 1
        mxcnt = max(mxcnt, cnt[c])
    symbs = sorted(cnt.keys())

    for i in range(mxcnt, 0, -1):
        for c in symbs:
            if i > cnt[c]:
                print(' ', end='')
            else:
                print('#', end='')
        print()
    print(''.join(symbs))
