# Ask for a date DD/MM/YYYY and display it in console
date = input("Enter your born date in the format DD/MM/YYYY: ")

# 10/11/2001

day = date[:date.find('/')]                  # 10/11/2001 = 10
monthYear = date[date.find('/')+1:]          # 10/11/2001 = 11/2001
month = monthYear[:monthYear.find('/')]      # 11/2001 = 11
year = monthYear[monthYear.find('/')+1:]     # 11/2001 = 2001

print(f"DAY: {day}, MONTH: {month}, YEAR: {year}")