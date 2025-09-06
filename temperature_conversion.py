unit  = input("is this temperature in celcius or farenheit (C/F) : ")
temp =  float(input("enter the temperature value : "))

if unit == "C":
    temp = round(temp *9/5 + 32, 2)
    print(f"the temperature in farenheit is : ",temp)

elif unit == "F":
    temp = round(temp- 32*5/9, 2)
    print(f"the temperature in celcius is  : ",temp)

else:
    print(f"the {unit} is invalid temperature unit")