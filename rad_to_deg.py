def rad_To_Deg():
    pi_Value=22/7
    rad_Value = float(input("Enter a number to convert to degree : "))
    deg_Value = rad_Value * (180/pi_Value)
    print(f" {rad_Value} Radian -> {deg_Value} Degreee")
rad_To_Deg()