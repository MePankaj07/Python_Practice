import math
def hex_Area():
    hex_Side = int(input("Enter side for Hexagon : "))
    hex__Area = ((3 * math.sqrt(3) *(hex_Side * hex_Side)) / 2)
    print(f"Hexagon area for side Value {hex_Side} = {hex__Area}")
hex_Area()