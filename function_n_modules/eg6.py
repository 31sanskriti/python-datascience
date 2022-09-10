def default_function (a=50,b = 100):
    return a+b

print (default_function())
print (default_function(a=99))
print (default_function())

def triangle_area(b,h=1):
    return .5*b*h
print(triangle_area(10))
print(triangle_area(5,3))
print(triangle_area(b=5))
print(triangle_area(b=7,h=5))


def read(filepath=None):
    if filepath:
        with open(filepath)as f:
            return f.read()

    else:
        return'please provide a filepath'

print(read('g1.py'))
print(read())
