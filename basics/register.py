print("Register your detail")
username = input("Enter the username")
Email = input("Enter the email")
Pass = input("Enter the password")
cpass = input("confirm password")
Gender = input("Enter the gender")

if len(username) > 4 and len(username) < 25 :
    if Email in '@' :
        if Pass == cpass :
            print("you are registered")
        else :
            print("password not matched")
    else:
        print("email is invaild")
else :
    print("username must be between 4 and 25 chars")
