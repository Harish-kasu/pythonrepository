p = float(input("enter the principal amount : "))
r = float(input("enter the value of interest rare (%) :"))
t = float(input("enter the time period in years "))

apr =  p*pow((1 + r/100),t)

print(f" the apr is : {apr:.3f}")

