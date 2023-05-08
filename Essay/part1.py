def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_euclidean(b, a % b)
    return gcd, y, x - (a // b) * y


def inverse_modulo(a, n):
    gcd, x, y = extended_euclidean(a, n)
    if gcd != 1:
        return None
    return x % n  # to make sure that the result is a positive integer between 0 and n - 1


print(inverse_modulo(8, 11))

print(inverse_modulo(6, 12))