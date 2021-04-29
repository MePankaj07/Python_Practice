def CelToFeh():
    Cel_Input = float(input("Ente a number to convert it to fehrenheit : "))
    ResFehren = (Cel_Input * 1.8) + 32
    print(f"{Cel_Input} degree Celsius to {ResFehren} degree Fehrenheit ")
CelToFeh()