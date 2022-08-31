#create a prime number list upto size n 
# 2, 3,5,7,11

prime =[]

for num in range(2,100):
    for x in range(2 , num):

        if num % x == 0:

            break
    else:
        prime.append(num)
for p in prime:
    print(p,end=',')


    

   
  