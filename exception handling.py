try:
    x = int(input('enter the value: '))
    print(1/x)

except ZeroDivisionError:
    print('do not divide by zero')

except TypeError:
    print('enter only number')

finally:
    print('cleanup')