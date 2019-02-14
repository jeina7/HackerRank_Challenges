import sys

N = int(sys.stdin.readline())
for _ in range(N):
    string = sys.stdin.readline().rstrip()
    even = [string[idx] for idx in range(len(string)) if not idx % 2]
    odd = [string[idx]for idx in range(len(string)) if idx % 2]
    sys.stdout.write("".join(even) + ' ' + "".join(odd) + '\n')
