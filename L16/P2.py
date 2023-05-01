import matplotlib.pyplot as plt
import pandas as pd

subjects = ["phy","chem","maths"]
marks =[87,56,74]

plt.plot(subjects,marks,color ="green",linewidth=5,marker="o",markersize=15,markerfacecolor="red")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Pranay Performance ")
plt.savefig("pranay.pdf")
plt.savefig("pranay.png")
plt.grid()
plt.show()
