# write a program that reads in 10 numbers, then prints the sum of those

total = 0

inpt = 0

while inpt < 10:
    try:
        total = total + int(input("Input a number: "))
        inpt = inpt + 1
    except ValueError:
        print("Please input number in its numerical form")

print(total)

