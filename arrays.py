num = int(input("enter a number : "))
k = int(input("enter the value of k : "))
n = "even " if num % 2 == 0 else "odd"
print(n)
s = "eligible" if k >= 18 else "not eligible "
print(s)
name =  input("enter your name : ")


print(name.find("h"))
print(name.rfind("p"))
print(name.upper())
print(name.capitalize())
print(name.replace("o", " "))
print(name.split("o"))

print(name.count("o"))
name = name[::-1]
print(name)
