
# Given an integer n, we are asked to write a function that is going to return the nth Fibonacci number in the Fibonacci sequence. Normally, the Fibonacci sequence uses zero based indexing, which means the first two numbers of the sequence are F0 = 0 and F1 = 1. However, in this problem, we are going to use one based indexing. For instance, getNthFib(1) should return 0 instead of 1.

def getNthFib(n):
    seq = [0,1]
    for t in range(1, n):
        seq.append(seq[t] + seq[t-1])
    return seq[n-1]