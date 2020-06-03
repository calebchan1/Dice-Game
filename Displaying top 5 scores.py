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
