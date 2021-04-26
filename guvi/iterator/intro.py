
# it uses two things iter and next
t1 = (11, '343')
l1 = iter(t1)
print(next(l1))

print(next(l1))

list1 = ['apple', 'mango']
l1 = iter(list1)

for x in list1:
    print(next(l1))
