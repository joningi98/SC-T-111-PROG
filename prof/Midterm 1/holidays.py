month = input("Month: ")
day = input("Day: ")

date_str = month.capitalize() + " " + day

if date_str == "January 1":
    print("New year's day")
elif date_str == "June 17":
    print("National holiday")
elif date_str == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")
