# Initiate the list
month_li = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Start infinite loop that breaks when a valid date is entered
while True:
    # Prompt the user for a date (format: 9/8/1636 or september 8, 1636)
    input_date = input("Date (in month/day/year order): ").strip()

    # Attempt to transform date into yyyy-mm-dd format
    try:
        # Check if date string starts not with a number but a letter
        if not input_date[0].isdigit():
            # Split the date by comma first
            month_day, year = input_date.split(",")

            # Split the month and day by space
            month, day = month_day.split(" ")

            # Convert day and year to integers; will deal with month after
            day = int(day.strip())
            year = int(year.strip())

            # Capitalize month for case insensitivity
            month = month.capitalize()

            # Need to check if the month exists in the list
            if month in month_li and (1 <= day <= 31):
                print(year,f"{month_li.index(month) + 1:02}", f"{day:02}", sep = "-")
                break

        else:
            # Split month, day and year by "/" separator and convert to integer
            month, day, year = map(int, input_date.split("/"))

            # Check whether month and day fall within expected ranges
            if 1 <= month <= 12 and 1 <= day <= 31:
                # If so, then print year, month, and date
                print(year,f"{month:02}",f"{day:02}", sep = "-")

                # Break out of the loop
                break

    except:
        pass
