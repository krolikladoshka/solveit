def frequentsymbol(s):
    q = {}
    for c in s:
        q[c] = q.setdefault(c, 0) + 1
    return max(q.items(), key=lambda x: x[1])[0]


def findmax(seq):
    if not seq:
        return
    mx = seq[0]

    for x in seq:
        if x > mx:
            mx = x
    return mx


def findmaxandsecond(seq):
    if not seq:
        return

    prevmx, mx = float('-inf'), float('-inf')

    for x in seq:
        if x > mx:
            prevmx = mx
            mx = x
        if mx > x and x > prevmx:
            prevmx = x

    return mx, prevmx

def findmaxandsecond1(seq):
    if not seq:
        return

    prevmx, mx = max(seq[0], seq[1]), min(seq[0], seq[1])

    for x in seq:
        if x > mx:
            prevmx = mx
            mx = x
        elif x > prevmx:
            prevmx = x

    return mx, prevmx

def findmineven(seq):
    if not seq:
        return -1
    m = -1

    for x in seq:
        if x % 2 == 0:
            if m == -1 or x < m:
                m = x
    return m


def shortwords(words):
    mlen = len(min(words, key=len))

    res = []
    for word in words:
        if len(word) == mlen:
           res.append(word)

    return res


def rle(s):
    if not s:
        return
    cnt = 0
    c = s[0]
    res = []

    for x in s:
        if x == c:
            cnt += 1
        else:
            res.append(c)
            if cnt > 1:
                res.append(str(cnt))
            c = x
            cnt = 1

    res.append(c)
    if cnt > 1:
        res.append(str(cnt))

    return ''.join(res)

def checkdictmiss(lst, dct):
    words = set()

    for word in dct:
        for i in range(len(word)):
            words.add(word[:i] + word[i + 1:])
    return list(map(lambda x: x in words, lst))
