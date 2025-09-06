email = input("Enter your email id : ")

index = email.index("@")

username =  email[:index:1]
domain = email[index + 1 : ]

print(f"your username is : {username} and your domain is : {domain}")
