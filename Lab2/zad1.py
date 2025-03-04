def is_prime(num):
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        return True
    return False


def prime_selector(numbers: list[int]):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)

    return primes


numbers = [1, 3, 4, 5, 1229, 1230, 4073, 4074, 7727, 7730]

primes = prime_selector(numbers)

print(primes)