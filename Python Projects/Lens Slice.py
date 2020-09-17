toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchoies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell {} differnt kinds of pizza!".format(num_pizzas))

print()

print("******************************")
pizzas = list(zip(prices, toppings))

print(pizzas)

print()

print("******************************")
pizzas.sort()

cheapest_pizza = pizzas[0]

print("Cheapest Pizza: " + str(cheapest_pizza))

print()

print("******************************")
priciest_pizza = pizzas[-1]

print("Most Expensive Pizza: " + str(priciest_pizza))

print()

print("******************************")
three_cheapest = pizzas[0:4]

print("Three Cheapest Pizza Varieties:")
print()
print(three_cheapest)

print()

print("******************************")

num_two_dollar_slices = prices.count(2)

print("Two dollar pizzas: ")
print(num_two_dollar_slices)
