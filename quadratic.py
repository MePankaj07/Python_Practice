import cmath
def QuadSol():

    a=float(input("Enter value for a : "))
    b=float(input("Enter value for b : "))

    c=float(input("Enter value for c : "))

    d = (b**2) - (4*a*c)  
    NegSol = (-b-cmath.sqrt(d))/(2*a)  
    PosSol = (-b+cmath.sqrt(d))/(2*a)  
    print(f"Negative  {NegSol} , Positive {PosSol}")  
QuadSol() 