PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

a=int(input("Enter the number of pennies: "))
b= int(input("Enter the number of nickels: "))
c=int(input("Enter the number of dimes: "))
d=int(input("Enter the number of quarters: "))

total_cents = (a*PENNY_VALUE) + (b*NICKEL_VALUE) + (c*DIME_VALUE) + (d*QUARTER_VALUE)

total_dollars = total_cents / PENNIES_IN_DOLLAR

if total_dollars > 1:
        print("Sorry, the amount you entered was more than one dollar.")
elif total_dollars < 1:
        print("Sorry, the amount you entered was less than one dollar.")
else:
        print("Congratulations!")
        print("The amount you entered was exactly one dollar!")
        print("You win the game!")