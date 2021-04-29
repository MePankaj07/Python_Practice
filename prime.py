num = int(input("Enter a number to find it is prime or not : "))
prime= True
for i in range(2, num):
    if(num%i==0):
        prime=False
if prime:
    print("Number is prime")
else:
    print("Number is not Prime")