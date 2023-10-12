data = list(input().split())
total = 0
leap_year = False
year_num = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = {
    'January': 1, 
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

# month
total += sum(year_num[:year[data[0]]])

# day
total += int(data[1].strip(',')) - 1

# year
if int(data[2]) % 400 == 0 or (int(data[2]) % 4 == 0 and int(data[2]) % 100 != 0):
    leap_year = True
    
    if year[data[0]] > 2:
        total += 1
    
# time
total += (int(data[3][0:2]) * 60 + int(data[3][3:5])) / 1440

# result
if leap_year:
    print(total * 100 / 366)
else:
    print(total * 100 / 365)