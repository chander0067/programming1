""" hireItems Function
function hireItems():
oprn file ("items.csv",'r')
read file f.readlines()
     set n=0
    hList=[]
for i in item:
        movieName = i.strip().split(',')[0]
        description = i.strip().split(',')[1]
        cost = float(i.strip().split(',')[2])
        availiblity = i.strip().split(',')[-1]

if availablity == "in":
            say (str(n)+" - "+"%-45s"%(movieName+"("+description+")")+"= $"+"%7.2f"%(cost),sep=" ")
            n+=1
            hList.append(i)

close file f.close()
while True:
movieChoice = int(input("Enter the number of an item to hire "))
if movieChoice >= 0 and movieChoice < n:

           open file in write mode f= open("items.csv",'w')

            m = item.index(hList[movieChoice])


            movie = item[m]
            movieName = movie.strip().split(',')[0]
            description = movie.strip().split(',')[1]
            cost = float(movie.strip().split(',')[2])
            print (movieName+ " hired for $"+ "%.2f" %(cost) )
            item[m] = movieName+","+description+","+str(cost)+","+"out\n"
            file=""
            for i in item:
            add a file after each execution    file = file + i
             write file say f.write(file)
            f close file say .close()
            break

        else:
            say ("Invalid input. \n")

"""
def hireItems():
    f= open("items.csv",'r')
    item= f.readlines()
    n=0
    hList=[]
    for i in item:
        movieName = i.strip().split(',')[0]
        description = i.strip().split(',')[1]
        cost = float(i.strip().split(',')[2])
        availiblity = i.strip().split(',')[-1]

        if availiblity == "in":
            print(str(n)+" - "+"%-45s"%(movieName+"("+description+")")+"= $"+"%7.2f"%(cost),sep=" ")
            n+=1
            hList.append(i)

    f.close()
    while True:
        movieChoice = int(input("Enter the number of an item to hire "))
        if movieChoice >= 0 and movieChoice < n:

            f= open("items.csv",'w')

            m = item.index(hList[movieChoice])


            movie = item[m]
            movieName = movie.strip().split(',')[0]
            description = movie.strip().split(',')[1]
            cost = float(movie.strip().split(',')[2])
            print (movieName+ " hired for $"+ "%.2f" %(cost) )
            item[m] = movieName+","+description+","+str(cost)+","+"out\n"
            file=""
            for i in item:
                file = file + i
            f.write(file)
            f.close()
            break

        else:
            print("Invalid input. \n")


"""LIST of MOVIES
# function listMovies() then say”All items on file(* indicates item is currently out)”
open file ("items.csv",'r')
     read file movie= f.readlines()
     set n=0
    for i in movie:
        movieName = i.strip().split(',')[0]
        discp = i.strip().split(',')[1]
        price = float(i.strip().split(',')[2])
        availablity= i.strip().split(',')[-1]

        print(str(n)+" - "+"%-45s"%(movieName+"("+discp+")")+"= $"+"%7.2f"%(price),sep=" ",end="")
        n+=1
        if item is all gone "out":
            say (" *")

        else:
            say ()
 close file ()
"""
def listMovies():
    print("All items on file (* indicates item is currently out):")
    f= open("items.csv",'r')
    movie= f.readlines()
    n=0
    for i in movie:
        movieName = i.strip().split(',')[0]
        discp = i.strip().split(',')[1]
        price = float(i.strip().split(',')[2])
        availablity = i.strip().split(',')[-1]

        print(str(n)+" - "+"%-45s"%(movieName+"("+discp+")")+"= $"+"%7.2f"%(price),sep=" ",end="")
        n+=1
        if availablity== "out":
            print(" *")

        else:
            print()
    f.close()


"""define a main function
function main()
a statement “Items for Hire- by Chander deep” will be printed on the screen
set numItem=numItems()
print’str(numItem)+items loaded from items.csv’

while true
set choice=input(enter your choice)
if choice=[‘l’,’L’] then say “listMovies”
elif choice=[‘h’,’H’] then say hireItems
elif choice=[‘r’,’R’] then say returnItems
elif choice=[‘a’,A] then say addItems
elif choice=[‘q’,’Q’] then say “have a nice day” and saved all items in ‘items.csv’
else say”invalid choice”
call function main()"""



#\\Main Function\\
def main():
    print ("Items for Hire - by Chander deep")
    count= countItems()
    print (str(count)+" items loaded from items.csv")

    while True:
        choice=input("Menu:\n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock\n(Q)uit \n\n")
        if choice in ['l','L']:
            listMovies()

        elif choice in ['H','h']:
            hireItems()

        elif choice in ['R','r']:
            returnItems()

        elif choice in ['A','a']:
            addItems()

        elif choice in ['q','Q']:
            count = countItems()
            print(str(count)+" items saved to items.csv \n Have a nice day :)")
            break

        else:
            print ("Invalid menu choice")



main()


