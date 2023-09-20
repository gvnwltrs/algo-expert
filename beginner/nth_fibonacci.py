def getNthFib(n):
    seq = [0,1]
    for t in range(1, n):
        seq.append(seq[t] + seq[t-1])
    return seq[n-1]