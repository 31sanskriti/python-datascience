x = int(input('order amount :'))
y = input("payment mode (cash , credit, upi):")
if x > 1000 :
    x -= x*0.03
if y == 'credit' :
    x-= 100
x += x*.18  #tax18%
print('your final amt is :', x)
 