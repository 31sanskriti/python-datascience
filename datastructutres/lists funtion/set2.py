my_set = {1,2}
print(my_set)

#add elements 
my_set.add(2)
print(my_set)

#add multiple elements
my_set.update([2,3,4])
print(my_set)

#add list and set 
my_set.update([4,5],{1,6,8})
print(my_set)

#remove and discard are same function 
my_set.discard(8)
print(my_set)

my_set.remove(5)
print(my_set)

#pop a random item
my_set.pop()
print(my_set)

#clear my_set
my_set.clear()
print(my_set)