print("Bill split generator:")

total_bill = float(input("What is the total bill: "))
total_tip = int(input("how much tip would you like to give? 10, 12, 15?"))
total_members = int(input("how many members are there to split:"))

tip_per = total_bill + (total_bill * (total_tip / 100))
total_amount = tip_per / total_members

final_bill = f"each member should pay: {total_amount}"
print(final_bill)
