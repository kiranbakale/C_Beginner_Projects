def sq(x):
    return x*x


numbers = [1, 4, 5, 6, 7]
done = map(sq, numbers)
print(list(done))
