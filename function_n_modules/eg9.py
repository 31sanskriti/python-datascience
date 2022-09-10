def getcubes(limit=10):
    for i in range(1, limit+10):
        yield i**3

for val in getcubes():
    print(val)

for val in getcubes(4):
    print(val)


def prime(start=2 , stop = 10):
    for num in range(start , stop):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            yield num
for p in prime(stop=100):
    print(p)


