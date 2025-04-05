def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(N, M):
    return (N * M) // gcd(N, M)

x = int(input())
y = int(input())

print(lcm(x,y))

