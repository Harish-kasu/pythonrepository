import time
sec =  int(input("enter the number of seconds to countdown from : "))

for i in reversed(range(sec)):
    seconds = i % 60
    minutes = int(i/60) % 60
    hours = int(i/3600) % 60 
    days = int(i/86400)
    time.sleep(1)
    
   
   
    print(f'{days:02}:{hours:02}:{minutes:02}:{seconds:02}')

time.sleep(1)
    



