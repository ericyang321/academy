# 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# a factor is a number that can be used to multiple another number to get target number
# num // factor = another factor
# 600 billion is an _extremely_ large number. we can't just find all it's factors and see which of the largest one is prime
# we also can't iterate on 600 billion.
# since factors are just multiples of 2 numbers, you can check numbers 0 -> sqrt(600 billion) instead of all 600 billion

from math import sqrt


def is_prime(n):
    # if it's an even number, it's definitely not a prime
    if n & 1 == 0:
        return False

    d = 3

    # checking up until the square root of the number is enough
    while d * d <= n:
        if n % d == 0:
            return False

        d += 2

    return True


def main():
    large_num = 600851475143

    for num in range(round(sqrt(600851475143)), -1, -1):
        if large_num % num == 0:
            print("divisible! checking if", num, "is prime...")
            if is_prime(num):
                return num

    return False
