choice = input("Press 1 for login else press any key for create new account : ")
if choice=='1':
    while True:
        mobile = input("Enter your contact number : ")
        if mobile.isdigit() and len(mobile)==10:
            password = input("Enter password : ")
            with open("loginaccount.txt") as f:
                for i in f:
                    j = i.split()
                    if mobile==j[0] and password==j[1]:
                        print("Your account verification successful")
                        exit()
                else:
                    print("Account verification unsuccessful")
        else:
            print("Enter valid number")

else:
    while True:
        mobile = input("Enter your contact number : ")
        if mobile.isdigit() and len(mobile)==10:
            with open("loginaccount.txt") as f:
                data = f.readlines()
                for i in data:
                    if mobile in i:
                        print('This number is already exist')
                        break
                else:
                    break
        else:
            print("Enter valid phone no.")
    while True:
        password = input("Enter your password : ")
        repassword = input("Enter your password again : ")
        if password==repassword:
            break
    with open("loginaccount.txt","a") as f:
        f.write(f"{mobile} {password}\n")
    print("Your account is created successfully")