# Slide Business Model Ventive
import numpy as np

ETH_price = np.array([2000, 3745.67, 5389.74, 8984.84, 13080]) # usd
eur_usd = 1.07
ETH_price = ETH_price/eur_usd
# print(ETH_price)
reached_people = 10500000
conversione = 0.0417
MoD_people = reached_people*conversione # al 5 anno

spesamedia_anni = [0, 0.003, 0.006, 0.009, 0.012] # ETH
user_anni = np.array([0, 25000, 110000, 220000, 440000])
n_scambi = [0, 2, 3, 7, 9]
Percentualeroyalties = 0.03

profit = 0
for i in range(5):
    yearly_profit = user_anni[i]*spesamedia_anni[i]*ETH_price[i]*n_scambi[i]*Percentualeroyalties
    # print(yearly_profit)
    profit += yearly_profit

crypto_people = user_anni*0.06
print(crypto_people)
average_investment = [0, 1000, 1100, 1200, 1300] # eur


monthly_performance = 2.32**(1/12)-1
# print(monthly_performance)
# 1/0
fee_percentage = 0.2

crypto_profit = 0
for i in range(5):
    crypto_yearly_profit = crypto_people[i]*average_investment[i]*monthly_performance*fee_percentage*12
    print(crypto_yearly_profit)

    crypto_profit += crypto_yearly_profit
