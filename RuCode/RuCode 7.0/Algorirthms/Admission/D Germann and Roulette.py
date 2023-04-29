def generate_sequences(n, k):
    def backtrack(seq):
        if len(seq) == k:
            print(' '.join(str(x) for x in seq))
            return
        start = seq[-1] + 1 if seq else 1
        for i in range(start, n+1):
            seq.append(i)
            backtrack(seq)
            seq.pop()
    backtrack([])

n, k = map(int, input().split())
generate_sequences(n, k)

# Python and c++ TL