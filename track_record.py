from cProfile import label
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

data = pd.read_excel('trades.ods')

# print(data)
# print(min(data['Profit']))
plt.figure()
plt.hist(data['Profit'], bins=300)
plt.grid()
plt.xlabel('Profit [%]')
plt.ylabel('Number of Trades')
plt.savefig('images/crypto/profithist.png', dpi=300)

plt.figure()
plt.hist(data['Profit'], bins=300, range=(-22, 32))
plt.grid()
plt.xlabel('Profit [%]')
plt.ylabel('Number of Trades')
plt.savefig('images/crypto/profithist2.png', dpi=300)

plt.figure()
plt.hist(data['Durata'], bins=300)
plt.grid()
plt.xlabel('Trade Length [minutes]')
plt.ylabel('Number of Trades')
plt.savefig('images/crypto/duratahist.png', dpi=300)

plt.figure()
plt.hist(data['Durata'], bins=300, range=(0, 10000))
plt.grid()
plt.xlabel('Trade Length [minutes]')
plt.ylabel('Number of Trades')
plt.savefig('images/crypto/duratahist2.png', dpi=300)

data2 = pd.read_excel('wallet_history.ods')
print(data2)
plt.figure()
plt.plot((data2['Compound']-1)*100, label="With Compound Interests")
plt.plot((data2['Non-Compound']-1)*100, label="Without Compound Interests")
plt.grid()
plt.xlabel('Days since 16th July 2021')
plt.ylabel('Profit [%]')
plt.legend()
plt.tight_layout()
plt.savefig('images/crypto/wallet.png', dpi=300)