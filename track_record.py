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
plt.savefig('images/crypto/profithist.png')

plt.figure()
plt.hist(data['Profit'], bins=300, range=(-22, 32))
plt.grid()
plt.xlabel('Profit [%]')
plt.savefig('images/crypto/profithist2.png')

plt.figure()
plt.hist(data['Durata'], bins=300)
plt.grid()
plt.xlabel('Durata [minutes]')
plt.savefig('images/crypto/duratahist.png')

plt.figure()
plt.hist(data['Durata'], bins=300, range=(0, 10000))
plt.grid()
plt.xlabel('Durata [minutes]')
plt.savefig('images/crypto/duratahist2.png')