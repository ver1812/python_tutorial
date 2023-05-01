import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("a.csv")
subjects = data["subjects"]
amit_marks = data["amit"]
sumit_marks = data["sumit"]
plt.plot(subjects, amit_marks, color="green",label="amit", linewidth=5, marker="o", markersize=15, markerfacecolor="red")
plt.plot(subjects, sumit_marks, color="blue",label="sumit", linewidth=5, marker="p", markersize=15, markerfacecolor="red")
plt.legend(shadow=True)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Amit Sumit Performance ")

plt.grid()
plt.show()

