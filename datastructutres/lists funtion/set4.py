
x= {'fans','AC','computers','phones','chargers'}
y={'light','TV','laptop','mouse','printer'}

#print(x.union(y))
#print(x.union(y))
#print(x.intersection(y))
#print(x.difference(y))
#print(x.symmetric_difference(y))
print(x|y)


ans = x.isdisjoint(y)
print(ans)

ans = x.issubset(y)
print("x is subset of all y : " , ans)

ans = x.issuperset({'fans','AC'})
print("x is superset of {fans,AC} :" ,ans)
