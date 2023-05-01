import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("p.csv")
subjects = data["subjects"]
marks = data["marks"]

plt.bar(subjects,marks,width=0.3,color=["blue",'yellow'])
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Pranay Performance ")
plt.show()