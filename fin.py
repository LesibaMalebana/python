year = int(input("What year do you want to start with "))
check_count = int(input("How many years do you want to check"))

for year in range(year, ):
    for check_count in range(year, check_count):
        if year % 4 == 0:
            print("{} is a Leap Year".format(year))
        else:
            print("{} Isn't a leap Year".format(year))
    print("Done")


