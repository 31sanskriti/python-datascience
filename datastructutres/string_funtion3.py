#strings startswith

value = input("enter the guest name:")

if value.startswith('Mr.'):
    print("welcome sir")
elif value.startswith("Ms."):
    print("welcome ma'am ")
elif value.startswith("Dr."):
    print("welcome doctor")
else:
    print("you are not invited")


