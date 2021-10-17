# sum of all the numbers from 1 upto n -> int
def linearsum(n):
    if n <= 0:
        return 0
    return (n * (n + 1)) // 2
