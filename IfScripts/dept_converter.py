def department_name(dep_code):
    if dep_code == 1:
        return "Department code 1 is: Marketing"
    elif dep_code == 5:
        return "Department code 5 is: Human Resources"
    elif dep_code == 10:
        return "Department code 10 is: Accounting"
    elif dep_code == 12:
        return "Department code 12 is: Legal"
    elif dep_code == 18:
        return "Department code 18 is: IT"
    elif dep_code == 20:
        return "Department code 20 is: Customer relations"
    else:
        return "Department code not identified."
    
    
user_input = int(input("Please enter your department code(whole numbers only): "))
dep_tranlator = department_name(user_input)
print(dep_tranlator)


#You can input an number into the input and the if/elif/else covers ever possible integer listed