expense = [2200,2350,2600,2130,2190]
print("The list is : ", expense)
print("\nExpense of January : ", expense[0])
print("Total expense in first quarter of the year : ", expense[0] + expense[1] + expense[2])

for amount in expense:
    if amount == 2000:
        flag = 1
        index = amount
    else:
        flag = 0
        

if flag == 1:
    print("In month ", index+1, " you have spent exactly Rs.2000")
else:
    print("You haven't spent exactly Rs.2000 in any month")

expense.append(1900)
print("List after adding June month expense")
print(expense)

expense[3] = 2130 - 200
print("List after making correction with refund in April")
print(expense)







