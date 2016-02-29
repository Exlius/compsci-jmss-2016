# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read
# write a program that reads in 10 numbers, then prints the sum of those

total = 0


run = True

while run:
    try:
        x = int(input("Input a number: "))
        if x == -1:
            run = False
        else:
            total = total + x

    except ValueError:
        print("Please input number in its numerical form")

print(total)

