my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #start zero through the last item
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods [0] ='cheese pizza'
print('friends food list',friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("after appending element into lists")
print(my_foods)
print(friend_foods)