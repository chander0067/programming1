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


