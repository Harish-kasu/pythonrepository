
txt = "welcome to the new page"

file_path = "C:/Users/kasuh/OneDrive/Desktop"

try:
    with open(csv_file.csv,"x") as f1:
        f1.write(txt)

except SyntaxError:
    print("something went wrong")

except PermissionError:
    print("some permission errors sorry")

finally:
    print("successfully done")


     
