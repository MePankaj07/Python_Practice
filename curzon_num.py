def is_Curzon():
    num = int(input("Input a Number to check it is curzon or not : "))
    if((2**num + 1)/(2*num +1)):
        print(f"{num} is Curzon")
    else: print(f"{num} is not Curzon")
is_Curzon()