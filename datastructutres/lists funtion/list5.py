#append function
fruits =[]
fruits.append("apple")
fruits.append("orange")
fruits.append("banana")
fruits.append("cherry")
fruits.append("23451")
print(fruits)

#insert function
fruits=["apple","banana","cherry"]
fruits.insert(-1,"orange")
print(fruits)

#extend function
fruits=["apple","banana","cherry"]
dry_fruits = ["walnut","almond","cashew"]
fruits.extend(dry_fruits)
print(fruits)

#remove function
fruits=["apple","banana","cherry","orange"]
fruits.remove("orange")
print(fruits)

#reverse funtion 
fruits=["apple","banana","cherry","orange"]
fruits.reverse()
print(fruits)

#sort funtion 
fruits=["apple","banana","cherry","orange"]
fruits.sort(reverse = True)
print(fruits)

#count funtion 
fruits=["3","45","56","78","89","45","90","58","45"]
fruits.count(45)
print(fruits)

#clear funtion 
fruits=["apple","banana","cherry","orange"]
fruits.clear()
print(fruits)

#list pop funtion 
fruits=["apple","banana","cherry","orange"]
fruits.pop()
print(fruits)
#pop index 
fruits1=["apple","banana","cherry","orange"]
fruits1.pop(2)
print(fruits1)
