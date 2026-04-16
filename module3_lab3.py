year = int(input("Enter a year: ")) # the code will take the users input to understand if its a common year or a leap year 


if year < 1582:
    print("Not within the Gregorian calendar period.")

elif year % 4 != 0:
    print("Common year")

elif year % 100 != 0:
    print("Leap year")

elif year % 400 != 0:
    print("Common year")

else:
    print("Leap year") 


