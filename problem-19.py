import numpy as np

def month_days(year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0) & (year % 400 != 0):
        days[1] = 29
    
    return days

def main():
    years = range(1900, 2001)
    months = []

    for year in years:
        months.append(month_days(year))

    data = np.array([[range(1, days + 1) for days in month]  for month in months])
    data_flattened = data.flatten()

    data = []
    for row in data_flattened:
        data.extend(row)
        
    sundays = 0
    for i in range(366, len(data)):
        if (i % 7 == 0) & (data[i] == 1):
            sundays += 1

    return sundays

if __name__ == "__main__":
    answer = main()
    print(answer)