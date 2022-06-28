# revenue bot da luglio a dicembre 2022. Crescita lineare.

def aum(x):
    m = 155
    q = 70
    return m*x+q

monthly_performance = 2.3**(1/10)-1
print(monthly_performance)
fee_percentage = 0.2

profit = 0
for i in range(6):
    # print(i)
    month_profit = aum(i)*monthly_performance
    # print(month_profit)
    profit += month_profit

print(profit)
ourprofit = profit*fee_percentage
print(ourprofit)