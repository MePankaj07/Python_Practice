lst = []


def lstEven():
    num = int(input("Enter a number : "))
    for i in range(1, num+1):
        if(i % 2 == 0):
            lst.append(i)
    print(lst)


lstEven()
