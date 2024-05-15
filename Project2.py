totalBill=float(input("Welcom to the tip calculator! \nWhat was the total bill? $ "))

tip = float(input("How much tip would you like to give? 10% , 12% , or 15%? "))
tip = totalBill*(tip / 100)

people = int(input("How many people to split bill? "))

bill = totalBill + tip
billEachPerson = bill / people

print(f"Each person should pay: ${round(float(billEachPerson) , 2)}")