import matplotlib.pyplot as plt

names = ["protein", "carbs", "fat"]
amt = [5.9, 73.3, 18.0]

plt.pie(amt, labels=names, autopct="%.2f%%",
        explode=[0, 0, 0.1], shadow=True)
plt.show()