#WAPP TO PRINT LOW AND HIGH
marks = ()
res = input("y : yes , n: no ")
while res == "y":
    m = int(input("enter marks "))
    marks = marks + (m,)
    res = input("do you want to enter more y/n")

low = min(marks)
high = max(marks)

print("low = ", low)
print("high = ",high)