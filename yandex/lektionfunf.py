def prefixsum(seq):
    ps = [0] * (len(seq) + 1)

    for i in range(1, len(seq) + 1):
        ps[i] = ps[i - 1] + seq[i - 1]
    return ps


def rsm(ps, l, r):
    return ps[r] - ps[l]


def prefzeroes(seq):
    ps = [0] * (len(seq) + 1)

    for i in range(1, len(seq) + 1):
        if seq[i - 1] == 0:
            ps[i] = ps[i - 1] + 1
        else:
            ps[i] = ps[i - 1]
    return ps


def prefzeroes1(seq):
    ps = [0] * (len(seq) + 1)

    for i in range(0, len(seq)):
        if seq[i] == 0:
            ps[i + 1] = ps[i] + 1
        else:
            ps[i + 1] = ps[i]
    return ps


def greaterk(seq, k):
    cnt = 0
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            print(seq[j], seq[i], seq[j] - seq[i])
            if seq[j] - seq[i] > k:
                cnt += 1
                print(cnt)
    print(cnt)

def greaterk1(seq, k):
    cnt = 0

    last = 0
    for i in range(len(seq)):
        while last < len(seq) and seq[last] - seq[i] <= k:
            last += 1
        cnt += len(seq) - last
    return cnt