mylist = [1,2,3,4,5]

try:
    x = mylist[5]
except IndexError:
    print("Out of range")
