#Store Prices
Apple_price = 2.50
Banana_price = 0.50
Tomato_price = 3.50
Bread_price = 3.50
#Shopping Cart
Apple_qty = 4
Banana_qty = 8
Tomato_qty = 7
Bread_qty = 2
#Total Cost
Total_Cost = (Apple_price * Apple_qty) + (Banana_price * Banana_qty) + (Tomato_price * Tomato_qty) + (Bread_price * Bread_qty)
#Budget
Budget = 30.00
#Check if within budget
if Total_Cost <= Budget:
    print("Total cost is within budget.")
else:
        print("You don't have enough money.")
        print("Total Cost: ", Total_Cost)
#Calculate remaining money if not within budget
Remaining_Money = Budget - Total_Cost
print("Remaining Money: ", Remaining_Money)