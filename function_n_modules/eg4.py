data = "" #global variable 
def data_appender(s):
    global data #this line tells data_appender that we have a global var data 
    if len(s) > 0:
        data += s

#call
data_appender('hello')
data_appender('world')
data_appender('this is a simple funtion')
data_appender('phle istemal kre phir vishwas kre')

print (data)

