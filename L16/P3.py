import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("p.csv")
subjects = data["subjects"]
marks = data["marks"]

plt.plot(subjects, marks, color="green", linewidth=5, marker="o", markersize=15, markerfacecolor="red")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Pranay Performance ")
plt.savefig("pranay.pdf")
plt.savefig("pranay.png")
plt.grid()
plt.show()
