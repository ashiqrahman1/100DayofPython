# Prime Number

def prime(number):
    check = True
    for x in range(2, number):
        if number % x == 0:
            check = False
    if check:
        print("Prime")
    else:
        print("Not Prime")


n = int(input("Enter a Number : "))
prime(n)
