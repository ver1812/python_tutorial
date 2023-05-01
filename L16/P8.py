from tkinter import *
import matplotlib.pyplot as plt

root = Tk()
root.title("Chart wallah")
root.geometry("600x600+50+50")
f = ("simsun", 30, "bold")

lab_name = Label(root, text="enter biscuit name ", font=f)
ent_name = Entry(root, font=f)
lab_name.pack(pady=5)
ent_name.pack(pady=5)

lab_protein = Label(root, text="enter protein ", font=f)
ent_protein = Entry(root, font=f)
lab_protein.pack(pady=5)
ent_protein.pack(pady=5)

lab_carbs = Label(root, text="enter carbs ", font=f)
ent_carbs = Entry(root, font=f)
lab_carbs.pack(pady=5)
ent_carbs.pack(pady=5)

lab_fat = Label(root, text="enter fat ", font=f)
ent_fat = Entry(root, font=f)
lab_fat.pack(pady=5)
ent_fat.pack(pady=5)


def gen():
    name = ent_name.get()
    protein = float(ent_protein.get())
    carbs = float(ent_carbs.get())
    fat = float(ent_fat.get())
    names = ["protein", "carbs", "fat"]
    amt = [protein, carbs, fat]

    plt.pie(amt, labels=names, autopct="%.2f%%",
            explode=[0, 0, 0.1], shadow=True)
    plt.title(name + " nutritional info ")
    plt.show()


btn_gen = Button(root, text="generate chart ", font=f, command=gen)
btn_gen.pack(pady=20)
root.mainloop()
