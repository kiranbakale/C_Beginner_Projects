def fun(variable):
    l = ['a', 'e', 'i', 'o', 'u']
    if(variable in l):
        return True
    else:
        return False
    seq = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
    filtered = filter(fun, seq)
    print("filtered letters are :")
    for seq in filtered:
        print(seq)
