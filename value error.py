try:
    number = int(input("enter a number: "))
    print("the number entered is error")
except ValueError as ex:
    print("exception", ex)