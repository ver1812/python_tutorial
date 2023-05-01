import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("a.csv")
amit_marks = data["amit"]
sumit_marks = data["sumit"]

subjects = data["subjects"]

x = np.arange(len(subjects))

plt.bar(x-0.12,amit_marks,label="amit",width=0.20)
plt.bar(x+0.12,sumit_marks,label="sumit",width=0.20)
plt.xticks(x,subjects)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.title("Amit Sumit Performance ")
plt.show()