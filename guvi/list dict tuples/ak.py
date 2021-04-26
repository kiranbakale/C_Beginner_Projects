list = [17, 19, 18, 10, 100, 5]
evencount = 0
oddcount = 0
for i in list:
    if(i % 2 == 0):
        print(i, "is even")
        evencount += 1

    elif(i % 2 != 0):
        oddcount += 1
        print(i, "is odd")
print("evencount is", evencount)
print("odd count", oddcount)
