def doubleChar():
    inpStr = input("Enter a string to check result : ")
    lst = []
    for i in range(len(inpStr)):
        res = inpStr[i]*2
        lst.append(res)
    print("".join(lst))


doubleChar()
