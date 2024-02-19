
def cycleFibonacci(n):
    if n == 0 or n == 1:
        return 1
    nMinusOne = 1
    nMinusTwo = 1
    for i in  range(2, n+1):
        nfibonacci = nMinusOne + nMinusTwo
        nMinusTwo = nMinusOne
        nMinusOne = nfibonacci
    return nfibonacci


for i in range(100):
    input()
    print (cycleFibonacci(i))


def recursiveFibonacci(n):
    if n == 0 or n == 1:
        return 1
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

for i in range(100):
    print(recursiveFibonacci(i))