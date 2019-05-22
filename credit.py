house_price = 1000000
down_payment_good = house_price * .1
down_payment_bad = house_price * .2

print("#############################")
print("Welcome to your down payment calculator!")
print("#############################")

credit = int(input("Do you have good credit? 1 for Yes, 0 for No: "))

if credit == 1:
    print("You have good credit!")
    print(f"Your down payment is: ${down_payment_good}")

elif credit == 0:
    print("You dont have good credit. :(")
    print(f"Your down payment is: ${down_payment_bad}")

else:
    print("You didn't answer 0 or 1. Please try again.")

