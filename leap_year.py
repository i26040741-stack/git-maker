start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))
for year in range (start_year, end_year + 1):
    if end_year <start_year:
        print("Invalid range. Please enter a valid range.")
    else:
        leap_years = []
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            leap_years.append(year)
            print(f"{leap_years} is a leap year.")
            print(f"The total number of leap years between {start_year} and {end_year} is: {len(leap_years)}")


