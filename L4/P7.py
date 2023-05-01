data =input("Enter String")
c1,c2 = 0,0

for d in data :
    if d.isalpha():
        if d in "aeiouAEIOU"       :
            c1+=1
        else    :
            c2+=1
print("Number of vowels = ",c1)
print("Number of con = ",c2)