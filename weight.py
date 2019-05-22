"""
ask for weight
    ask if Lbs or Kg
convert to opposite
display result
"""

weight = int(input("Weight?: "))
lbs_or_kg = (input("(L)bs or (K)g?: ")).lower()

if lbs_or_kg == "k" or lbs_or_kg == "K":
    print("Converting Kg to Lbs...")
    print(f"You weigh {weight * 2.20462} lbs.")

elif lbs_or_kg == "l" or lbs_or_kg == "L":
    print("Converting Lbs to Kg...")
    print(f"You weigh {weight * 0.453592} kg.")

else:
    print("Unrecognized input. Please use 'L' or 'K'.")

