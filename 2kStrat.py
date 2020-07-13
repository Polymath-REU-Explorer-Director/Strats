import sys

if (len(sys.argv) != 2):
    print("error: requires 1 parameter - integer k for 2^k vertices")
    exit()

k = int(sys.argv[1])
print("playing on 2^%d vertex cycle" %(k))
n = 2**k
numMoves = n - 1

moves = [None]*numMoves
div = 1
for i in range(k):
    div = div*2
    move = n//div
    for j in range(div//2-1, n-1, div):
        moves[j] = move

print(moves)
