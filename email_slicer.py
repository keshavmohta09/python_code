email = input("Enter your mail id: ")
username = ''
domain = ''
for i in range(len(email)):
    if email[i]!='@':
        username=username+email[i]
    else:
        print("Username: ", username)
        for j in range(i+1,len(email)):
            if email[j]!='.':
                domain = domain+email[j]
            else:
                print("Domain: ",domain)