#question
#create a contact dict , where the user can search for a person name
# and if the name exists , it display the phne number
#else, the user should be provided a choice to add the phne no. of that person.
#also the user can choose to list all the person and numbers.

#code 
contacts = {
    'emergency': 101,
    'police': 100
}

while True:
    print('# options')
    print('1️⃣  Search person')
    print('2️⃣  View all')
    print('3️⃣  Exit')
    ans = input("enter a number: ")
    if ans  == '1':
        name = input("enter the persons' name: ")
        if name in contacts:
            print(f"👉 {name} => {contacts[name]}")
        else:
            print(f"Not found, would you like to add the {name}s' number?")
            number = input(f'enter number for {name} =>')
            contacts[name] = number
            print('details added')
    elif ans == '2':
        for name, number in contacts.items():
            print(f'👉 {name} => {number}')
    elif ans == '3':
        print("BYE")
        break
    else:
        print("⚠️ wrong input ⚠️")

