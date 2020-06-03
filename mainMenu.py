
#Main Menu of dice Game
print("Welcome to the multiplayer Dice Game, please enter 1,2 or 3")
option = input("1. Log in\n2. Create a New User\n3. Quit")
#End variable is used to contiounsly loop the option chosen in the menu
end=False
valid=False
while end==False:
    
    #Logging in
    if option == "1":
        username = input("Please enter your username")
        #To check if the user has not entered nothing
        while len(username)==0:
            username=input("You have not entered anything\nPlease enter your username")
        password = input("Please enter your password")
        while len(password)==0:
            password=input("You have not entered anything\nPlease enter your password")
        #This will judge if the cridentials are valid or not
        usersfile = open("users.txt","r")
        users=usersfile.readlines()

        #Using for loop to check through each line whether or not
        #the credientials given are valid(found in the folder)
        for row in users:
            row=row.strip("\n")
            row=row.split(",")
            
            if username == row[0] and password == row[1]:
                valid=True
                print("User has been validated")
                end=True
        if valid==True:
            break
        print("User has not been validated please try again")
        usersfile.close()
        
    #Creating a new user
    elif option == "2":
        
        print("You have selected to create a new user")

        #Creating a new username
        newusername = input("Please enter a username")
        #To check if the user has not entered nothing
        while len(newusername)==0:
            newusername=input("You have not entered anything\nPlease enter a username")

        #Creating a new password
        newpassword = input("Please enter a password\nThe password must be more than 8 characters, for example john7atschool")
        #To check if the user has not entered nothing
        while len(newpassword)==0:
            newpassword=input("You have not entered anything\nPlease enter a password")
        while len(newpassword)<7:
            newpassword=input("You have not entered a password that is more than 8 characteres")

        #Writing user cridentials to a file
        usersfile = open("users.txt","a+")
        usersfile.write(newusername+","+newpassword+"\n")
        usersfile.close()
        valid=True
        end=True

    elif option=="3":
        #Allowing the user to quit the program if they chose option 3
        end=True
        
    
    
       
