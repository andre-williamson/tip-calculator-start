#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
print("     TIP CALCULATOR ")

bill = float(input("how much was the total bill: $ :" ))
tip = int(input("how much do you want to tip, 12 15  20 :"))
guest = int(input("How many guest: "))     

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
Bill_per_person = total_bill / guest
final_amount = round(Bill_per_person, 2)

print(f"Everybody should pay: ${final_amount}")





