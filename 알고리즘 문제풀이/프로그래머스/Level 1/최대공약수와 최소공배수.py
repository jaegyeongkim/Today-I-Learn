def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return x*y//gcd(x, y)
    

def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    
    return answer




