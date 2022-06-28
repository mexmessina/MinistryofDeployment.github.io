import matplotlib.pyplot as plt

marketing = 233800

defi_red = 222000

p_red = 252850

gea = 157500
workingcapital = 30000 

total = marketing+defi_red+p_red+gea+workingcapital
ratio = 600000/total
print(ratio)

marketing *= ratio
print(marketing)
defi_red *= ratio
print(defi_red)
p_red *= ratio
print(p_red)
gea *= ratio
print(gea)
workingcapital *= ratio
print(workingcapital)

ex = 0.2
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Marketing', 'DeFi R&D', 'Platform R&D', 'G&A', 'Working Capital'
sizes = [marketing, defi_red, p_red, gea, workingcapital]
explode = (ex, ex, ex, ex, ex)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('profithist2.png', dpi=300)