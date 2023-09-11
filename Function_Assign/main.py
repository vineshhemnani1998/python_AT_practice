def per(mobt, mtot):
    return mobt / mtot * 100
mobt = int(input("Enter Obtain Marks: "))
mtot = int(input("Enter Total  Marks: "))
result = per(mobt, mtot)
if result >= 40:
    print("you are pass")
else:
    print("you are fail")   
print(result)     