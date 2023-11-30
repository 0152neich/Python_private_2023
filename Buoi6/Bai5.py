def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(ts, ms):
    gcd = find_gcd(ts, ms)
    simple_ts = ts // gcd
    simple_ms = ms // gcd
    return simple_ts, simple_ms

def product_of_fractions(n):
    total_ts = 1
    total_ms = 1

    for _ in range(n):
        a, b = map(int, input().split())
        total_ts *= a
        total_ms *= b

    gcd = find_gcd(total_ts, total_ms)
    simple_ts = total_ts // gcd
    simple_ms = total_ms // gcd

    return simple_ts, simple_ms

n = int(input())
result_ts, result_ms = product_of_fractions(n)
print(result_ts, result_ms)
