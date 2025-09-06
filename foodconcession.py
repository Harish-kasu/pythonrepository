menu = {
    "pizza": 5.0,
    "nachos": 3.0,
    "popcorn": 2.5,
    "fries": 2.0,
    "soda": 1.5
}

cart =[]
total_items = 0

print("-----------MENU-----------")
for i,p in menu.items():
    print(f"{i} $ {p:.2f}")

print("---------------------------")

while True:
     item = input("please enter the items you want (q to quit):").lower()
     if item == "q":
          break
          if item  in menu:
              continue
          else :
               print("item not in menu")
               
     