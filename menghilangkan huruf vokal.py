x = "AaIiUuEeOo"
y = input("masukkan kata ==> ")
for letter in x:
    if letter in y:
        y = y.replace(letter,"")
print(y)