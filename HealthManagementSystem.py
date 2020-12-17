class HealthManager:
    def __init__(self,name,age,weight,height):
        self.name = name+'|'
        self.age = age+'|'
        self.weight = weight+'|'
        self.height = height+'|'

    def newdatasave(self):
        details = self.name+self.age+self.weight+self.height+'\n'
        file = open('HealthManager.txt','a')
        file.write(details)
        file.close()

    @classmethod
    def takeinput(cls,name):
        while True:
            age = input("Enter your age : ")
            if age.isdigit():
                break
            print("Enter the valid age")
        while True:
            weight = input("Enter your weight in kg: ")
            try:
                weight = float(weight)
                weight = str(weight)
                break
            except:
                print("Enter the valid weight")
        while True:
            height = input("Enter your height in inches : ")
            if height.isdigit():    break
            print("Enter the valid height")
        BMI = float(weight)/((int(height)*0.0254)**2)
        print(f'\nYour BMI = %.2f'%(BMI))
        if BMI<18.5:    print("You are Underweight")
        elif BMI>24.9:  print("You are Overweight")
        else:   print("Your weight is Normal")
        return cls('Name : '+name,'Age : '+age,'Weight(kg) : '+weight,'Height(inch) : '+height)

    @staticmethod
    def checkinfile(name):
        file = open('HealthManager.txt')
        while True:
            line = file.readline()
            if line=='':    break
            line = line.split('|')
            if name in line[0]:
                weight, height = line[2].split(':'), line[3].split(':')
                weight, height = float(weight[1].strip()), int(height[1].strip())
                BMI = weight/((height*0.0254)**2)
                if BMI<18.5:    i = "\nYou are Underweight"
                elif BMI>24.9:  i = "\nYou are Overweight"
                else:   i = "\nYour weight is Normal"
                BMI = f'Your BMI = %.2f'%(BMI)+i
                line.append(BMI)
                return '\n'.join(line)
        file.close()
        return None

while True:
    name = input("Enter your name [>5 characters]: ")
    if len(name)<5: print('Input minimum 5 characters')
    else:   break
isdata = HealthManager.checkinfile(name)
if isdata!=None:
    print(isdata)
else:
    print("Your data not found.....")
    save = input("Press 1 for create new account : ")
    if save=='1':
        newuser = HealthManager.takeinput(name)
        newuser.newdatasave()