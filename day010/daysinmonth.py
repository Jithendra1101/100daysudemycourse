def leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    year = int(input("Enter year : "))
    month = int(input("Enter month : "))
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12:
        print("Invalid month")
        month = int(input("Enter corect month : "))
    if leapyear(year):
        if month == 2:
            print("There are 29 days in that month")
        else :
            print("There are", day_in_month[month - 1], "days in that month")
    else:
        print("There are", day_in_month[month - 1], "days in that month")
        
main()