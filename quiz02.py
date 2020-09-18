print("You have 100 dollars left.")
print("Each cupcake costs 5 dollars.")
buy_cupcakes = int(input("How many cupcakes are you buying?"))
remain_money = 100 - buy_cupcakes*5
print("You have",remain_money,"dollars left.")
print("Each apple costs 2 dollars.")
buy_apples = int(input("How many apples are you buying?"))
remain_money = remain_money - buy_apples*2
print("You have",remain_money,"dollars left.")
guests = int(input("How many people are at the party?"))
cupcake_allocate = buy_cupcakes // guests
leftover_cake = buy_cupcakes % guests
apples_allocate = buy_apples // guests
leftover_apple = buy_apples % guests
print("Each guest can have",cupcake_allocate, "cupcakes.")
print("There will be", leftover_cake ,"cupcakes left over.")
print("Each guest can have", apples_allocate, "apples.")
print("There will be",leftover_apple, "apples left over.")
calories = (leftover_cake*240)+(leftover_apple*95)
print("The leftovers are worth", calories "calories.")
