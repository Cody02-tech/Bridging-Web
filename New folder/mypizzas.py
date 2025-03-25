pizzas = ['Califonia pizza', 'Greek pizza', 'Cheese pizza', 'Burger pizza']
friend_pizzas = pizzas[:]
pizzas.append ('pineapple pizza')
friend_pizzas.append('hawaii pizza')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
