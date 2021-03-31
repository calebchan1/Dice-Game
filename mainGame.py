import random
import time

def readfile(filename):
    file = open(filename,"r")
    contents = file.readlines()
    file.close()
    return contents

def writefile(filename,entry):
    file = open(filename,"a+")
    file.write(entry)
    file.close()

    
def mainMenu():
    #Main Menu of dice Game
    print("Welcome to the multiplayer Dice Game, please enter 1,2 or 3")
    option = input("1. Log in\n2. Create a New User\n3. Quit\n")
    #End variable is used to contiounsly loop the option chosen in the menu
    end=False
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
            users = readfile("users.txt")
            #Using for loop to check through each line whether or not
            #the credientials given are valid(found in the folder)
            for row in users:
                row=row.strip("\n")
                row=row.split(",")
                if username == row[0] and password == row[1]:
                    print("User has been validated")
                    return True
            print("User has not been validated please try again")
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
            writefile("users.txt",newusername+","+newpassword+"\n")
            return True
        elif option=="3":
            #Allowing the user to quit the program if they chose option 3
            return False
    
#Creating a function called score() which will return back the scores of two random dices
def score():
    import random
    #Imported random libary to generate two random numberse
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    return dice1,dice2
    
def displayDice():
    print("000000000000")
    print("0          0")
    print("0  #    #  0")
    print("0    #     0")
    print("0  #    #  0")
    print("0          0")
    print("000000000000")
    
if mainMenu() == True:
    #Start of dice game code
    rounds = 0
    total1 = 0
    total2 = 0
    #Introductary for when the game will start
    for i in range(3,0,-1):
        print("Starting the game in",i)
        time.sleep(1)
    #Will always loop code before rounds>5
    while rounds<5:
        #Player 1's turn
        print("Player 1's turn")
        time.sleep(3)
        score1=score()
        total1=total1+score1[0]+score1[1]
        #Rolling a double
        if score1[0]==score1[1]:
            print("Player 1 rolled a", score1[0],"and a",score1[1])
            time.sleep(1)
            print("Player 1 gets to roll again")
            time.sleep(1)
            #User will roll another dice, which adds to their total score
            dice=random.randint(1,6)
            print("Player 1 rolled a",dice)
            total1=total1+dice
            time.sleep(1)
            print("Player 1 gained",dice+score1[0]+score1[1],"points")
            time.sleep(3)
        else:
            #Adding both dices together to one variable, since we know it is not double
            totaldicescore1=score1[0]+score1[1]
            #Rolling an even
            if totaldicescore1%2==0:
                print("Player 1 rolled a total of",totaldicescore1)
                time.sleep(1)
                print("Player 1 rolled an even total! Add 10!")
                total1=total1+10
                time.sleep(1)
                print("Player 1 gained",totaldicescore1+10,"points")
                time.sleep(3)
            #Rolling an odd
            elif totaldicescore1%2==1:
                print("Player 1 rolled a total of",totaldicescore1)
                time.sleep(1)
                print("Player 1 rolled an odd total! Subtract 5!")
                total1=total1-5
                time.sleep(1)
                print("Player 1 gained",totaldicescore1-5,"points")
                time.sleep(3)
            
        #Player 2's turn
        print("\n")
        print("Player 2's turn")
        time.sleep(3)
        score2=score()
        total2=total2+score2[0]+score2[1]
        #Rolling a double
        if score2[0]==score2[1]:
            print("Player 2 rolled a", score2[0],"and a",score2[1])
            time.sleep(1)
            print("Player 2 gets to roll again")
            time.sleep(1)
            #User will roll another dice, which adds to their total score
            dice=random.randint(1,6)
            print("Player 2 rolled a",dice)
            total2=total2+dice
            time.sleep(1)
            print("Player 2 gained",dice+score2[0]+score2[1],"points")
            time.sleep(3)
          
        else:
            #Adding both dices together to one variable, since we know it is not double
            totaldicescore2=score2[0]+score2[1]
            #Rolling an even
            if totaldicescore2%2==0:
                print("Player 2 rolled a total of",totaldicescore2)
                time.sleep(1)
                print("Player 2 rolled an even total! Add 10!")
                total2=total2+10
                time.sleep(1)
                print("Player 2 gained",totaldicescore2+10,"points")
                time.sleep(3)
            #Rolling an odd
            if totaldicescore2%2==1:
                print("Player 2 rolled a total of",totaldicescore2)
                time.sleep(1)
                print("Player 2 rolled an odd total! Subtract 5!")
                total2=total2-5
                time.sleep(1)
                print("Player 2 gained",totaldicescore2-5,"points")
                time.sleep(3)
        #Checks that the total score of each player does not equal to 0
        if total1<0:
            total1=0
        elif total2<0:
            total2=0
        print("Round",rounds+1,"over")
        rounds=rounds+1
        time.sleep(1)
        print("Player 1 has a total of...\n",total1)
        print("Player 2 has a total of...\n",total2)
        time.sleep(3)

    #Displaying who has won
    if total1>total2:
        winnerscore=total1
        print("Player 1 has won!\nScoring",total1,"points!!")
        displayDice()

    elif total1<total2:
        winnerscore=total2
        print("Player 2 has won!\nScoring",total2,"points!!")
        displayDice()

    elif total1==total2:
        print("You two drew, roll one die each\nWhoever has highest wins")
        
        #While loop generates random dices, until one player has the higher score than the other
        while total1==total2:
            dices=score()
            total1=dices[0]+total1
            print("Player 1 rolled",dices[0])
            time.sleep(1)
            total2=dices[1]+total2
            print("Player 2 rolled",dices[1])
        #Displays who has won, after rolling again
        if total1>total2:
            winnerscore=total1
            print("Player 1 has won!\nScoring",total1,"points!!")
            displayDice()

        elif total1<total2:
            winnerscore=total2
            print("Player 2 has won!\nScoring",total2,"points!!")
            displayDice()
            
    #Saving the winner's name and score in an external file
    winnername=input("Winner, please enter your name")
    winnersFolder=open("winners.txt","a+")
    winnersFolder.write(winnername+","+str(winnerscore)+"\n")
    winnersFolder.close()

    #Displaying the top 5 scores
    winnersFolder=open("winners.txt","r")
    winners=winnersFolder.readlines()
    #Sorting through each index in the folder
    #In order to sort, I must save the top scores as a list
    topscores=[]
    for row in winners:
        row=row.strip("\n")
        row=row.split(",")
        topscores.append(row[1])

    #.sort will sort the list into an order
    #by using reverse=True, this will sort the list into descending order
    topscores.sort(reverse=True)
    #Finding the winner name of the scores

    #Using a count-controlled for loop, this will print out the top 5 scores
    for row in range(5):
        #I will make a match variable that changes depending on a match
        match = False
        while match == False:
            #using i to represent each index of the winners array
            for i in winners:
                i=i.strip("\n")
                i=i.split(",")
                #if the 1st row in topscores matches with the second index(where
                #scores are saved), than match will become True
                if topscores[row]==i[1]:
                    match = True
                    print(i[0],"scored a total of",topscores[row],"points")
    time.sleep(1)



   
        
        
              
