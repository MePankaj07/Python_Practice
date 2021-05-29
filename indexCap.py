lst = []


def indexCap():
    inpStr = input("Enter a string : ")
    for i in range(len(inpStr)):
        if(inpStr[i].isupper()):
            res = i
            lst.append(res)
            continue
    print(lst)


indexCap()
