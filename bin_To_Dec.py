def bin_To_Dec():
    bin_num = int(input("Enter a number : "))
    dec = 0
    i = 1
    while bin_num!=0:
        rem = bin_num%10
        dec = dec + (rem*i)
        i = i*2
        bin_num = int(bin_num/10)
    print(f"Binary Number -> {dec} Decimal Number")
bin_To_Dec()