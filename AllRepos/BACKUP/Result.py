##from collections import Counter
##
##words = []
##for _ in range(int(input())):
##    words.extend(input().split())
##
##counter = Counter(words)
##pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
##words = [pair[1] for pair in sorted(pairs)]
##print('\n'.join(words))

# You can also solve this problem without Counter:

n = int(input())
counts = {}
for _ in range(n):
    for word in input().split():
        counts[word] = counts.get(word, 0) + 1

freqs = [(-count, word) for (word, count) in counts.items()]
for c, word in sorted(freqs):
    print(word)