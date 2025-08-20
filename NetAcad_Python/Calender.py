year = int(input("Enter a year: "))

y1 = "common year"
y2 = " leap year"

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print(y1)
    elif year % 100 != 0:
        print(y2)
    elif year % 400 != 0:
        print(y1)
    else: 
        print(y2)