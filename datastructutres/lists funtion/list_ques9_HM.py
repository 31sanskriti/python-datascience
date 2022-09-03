#question -2 
#wap to create a list and then replace all the value greater than 5 by 0

list = [3, 4, 7, 5, 6, 7, 3, 4, 6, 9]
print(list)
x = 5
replace_chr = "0"
ans = [replace_chr if i > x else i for i in list]
 
print(ans)

#question-3
#wap to create a list that contains 5 small sublist of 3 items each (nested list)
#take the input from the user and to create this nested list. 
 