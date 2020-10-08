class contactbook:

    def savecontact(self,name,number,email,address):
        details = f"Name = {name} | Contact no. = {number} | E-mail = {email} | Address = {address}\n"
        file = open("contactdirectory.txt","a")
        file.write(details)
        file.close()
        print("Your contact saved in 'contactdirectory.text' file.")

    def searchcontact(self,nameornumber):
        if nameornumber.isdigit() is False: temp = 0
        else:   temp = 1
        file = open("contactdirectory.txt")
        while True:
            line = file.readline()
            if line == '':
                exit()
            line = line.split(' | ')
            if nameornumber in line[temp]:
                print()
                for item in line:
                    print(str(item))
        file.close()
        exit()

contact = contactbook()
while True:
    choice = input("Enter 1 for save the contact else press 2 for search the contact: ")
    if choice=='1':
        name = input("Enter name: ")
        print("Enter number: ",end='')
        while True:
            number = input()
            if number.isdigit() is True:
                break
            print("Enter correct number: ", end='')
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact.savecontact(name,number,email,address)
        break
    elif choice=='2':
        nameornumber = input("Enter the name/number: ")
        contact.searchcontact(nameornumber)
    else:
        print("Enter the correct number")