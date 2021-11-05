email = input("Please enter your email : ")
if(email.find("@")>0):
    if(email.find(".")>0):
        print(email," is a valid e-mail.")
    else:
        print(email," is not a valid e-mail.")