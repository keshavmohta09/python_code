string = input("Enter the string : ")
sub_string = input("Enter the sub-string : ")
end_index = len(sub_string)
start_index = 0
if sub_string in string:
    for i in range(len(string)):
        temp = string[i:end_index]
        if sub_string==temp:
            print(f"Start Index : {start_index}\nEnd Index : {end_index-1}")
            break
        else:
            start_index+=1
            end_index+=1
else:
    print("Substring is not present in string.")