"""3-6. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
 • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the 
end of your program, informing people that you found a bigger table.
 • Use insert() to add one new guest to the beginning of your list.
 • Use insert() to add one new guest to the middle of your list.
 • Use append() to add one new guest to the end of your list.
 • Print a new set of invitation messages, one for each person in your list."""


friends = ['Cody','Kan','Yer Yer']
print("Wow we've got a bigger dinner table.")
friends.insert(0, 'Kan Kan')
friends.insert(2, 'Yuri')
friends.append('Zin')
print(f"{friends[0]}, please  join the dinner Tonight!")
print(f"{friends[1]}, please  join the dinner Tonight!")
print(f"{friends[2]}, please  join the dinner Tonight!")
print(f"{friends[3]}, please  join the dinner Tonight!")
print(f"{friends[4]}, please  join the dinner Tonight!")
print(f"{friends[5]}, please  join the dinner Tonight!")


print("Sorry. there is only two people we can invite for dinner")
print(f"{friends.pop()} ")


print(f"{friends[0]}, you are still invited")
print(f"{friends[1]}, you are still invited")