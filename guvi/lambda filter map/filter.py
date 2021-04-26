def prime(x):
    for n in range(2, x):
        if(x % n == 0):
            return False
        else:
            return True


numbers = [1, 33, 55, 67, 88]
done = map(prime, numbers)
print(list(done))
# def prime(x):
#     for n in range(2, x):
#         if(x % n == 0):
#             return False
#         else:
#             return True

# Filtered = filter(prime, range(10))
# print("the prime numbers are ", list(Filtered))
