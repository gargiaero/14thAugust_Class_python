def sum_of_primes(list1):
    s = 0
    for num in list1:
        i = 2
        p = 1
        while i <= num / 2:
            if num % i == 0:
                p = 0
                break
            i = i + 1
        if p == 1:
            s = s + num
    return s


list1 = [2,3,5,7,11,13]
s = sum_of_primes(list1)
print("Sum of all prime numbers:", s)