weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")
if unit == 'l':
    weight_lbs = weight * 0.45
    print(f"{weight_lbs} kilos")
elif unit == 'k':
    weight_kg = int(weight) /0.45
    print(f"{weight_kg} pounds")