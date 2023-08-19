daily_sales = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)#amount days

reduce_day = 0#start from 0

for i in range(1, len(daily_sales)):#i start from 1to 10
    if daily_sales[i] < daily_sales[i - 1]:#compare if index i in daily_sales lower than index i-1 count 1
        reduce_day += 1#start from 0 the first 0+1

print("Number of days with reduced sales:", reduce_day)