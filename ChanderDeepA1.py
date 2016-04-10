l"""RETURN ITEMS
function returnItems():
          open file in read mode
          item= f.readlines()
          set n=0
          hList=[]
          for i in  item list with some information about item:
              movieName = i.strip().split(',')[0]
              description = i.strip().split(',')[1]
              cost = float(i.strip().split(',')[2])
              availiblity = i.strip().split(',')[-1]

               if availiblity == "out":
                    say (str(n)+" - "+"%-45s"%(movieName+"("+description+")")+"= $"+"%7.2f"%(cost),sep=" ")
                     n+=1
                     hList.append(i)

         close file
         while True:

               print msg
               choice = int(input("Enter the number of an item to return "))

                if choice >= 0 and choice < n:


                         open a file in write so that it change the file with new information
                        f= open("items.csv",'w')

                             m = item.index(hList[choice])


                              movie = item[m]
                               movieName = movie.strip().split(',')[0]
                              description = movie.strip().split(',')[1]
                              cost = float(movie.strip().split(',')[2])
                               say (movieName+ " returned")
                               item[m] = movieName+","+description+","+str(cost)+","+"in\n"
                               file=""
                                for i in item:
                                file = file + i
                                f.write(file)
                                 f.close()
                                 break

        else:
            say ("Invalid item number")"""


def returnItems():
    f= open("items.csv",'r')
    item= f.readlines()
    n=0
    hList=[]
    for i in item:
        movieName = i.strip().split(',')[0] #first object of list goes to movieName
        description = i.strip().split(',')[1]#2 object of list goes to description
        cost = float(i.strip().split(',')[2])#3 object is cost
        availiblity = i.strip().split(',')[-1]#last object is weather it is available or not

        if availiblity == "out":
            print(str(n)+" - "+"%-45s"%(movieName+"("+description+")")+"= $"+"%7.2f"%(cost),sep=" ")#format statement
            n+=1
            hList.append(i)

    f.close()
    while True:

        choice = int(input("Enter the number of an item to return "))

        if choice >= 0 and choice < n:
            f= open("items.csv",'w')

            m = item.index(hList[choice])# index of choosen item from the file in m


            movie = item[m]
            movieName = movie.strip().split(',')[0]
            description = movie.strip().split(',')[1]
            cost = float(movie.strip().split(',')[2])
            print (movieName+ " returned")
            item[m] = movieName+","+description+","+str(cost)+","+"in\n"
            file=""
            for i in item:
                file = file + i
            f.write(file)
            f.close()
            break

        else:
            print("Invalid item number")


""" function countItems()
             open file "Items.csv" in read mode
             items = f.readlines()
              length of the item
              count=len(items)
              return len

LENGTH LIST"""

def countItems():# function to count the number of ites in the file Items.csv
    f= open("Items.csv",'r')
    items = f.readlines()
    count= len(items)
    return count

"""def addItems():
          if while loop is true
                 movieName = input("Item Name: ")
                 and movie name empty if movieName =="":
                 say ("Input cannot be blank")
          else:
               break statement with
               description = input("Description: ")

              if loop is true
          while True:
                 costStr = input("Price per day: $")
                 if loop
                 if costStr.isalpha():
                 say ("Invalid number; enter a valid number")
                again elif loop
                 elif float(costStr) < 0:
                       print("Price must be >= $0 \n Invalid input; enter a valid number")

                 else:
                      cost= float(costStr)
                       break

          print(movieName+" ("+description+"), $"+str("%-0.2f" %(cost))+ " now available for hire")
           f = open("Items.csv", 'a')
           new = movieName+","+description+","+str(cost)+","+"in\n"
           f.write(new)
           f.close()
ADD ITEMS"""



def addItems():
    while True:
        movieName = input("Item Name: ")
        if movieName =="":
            print("Input cannot be blank")
        else:
            break
    description = input("Description: ")

    while True:
        costStr = input("Price per day: $")
        if costStr.isalpha():
            print("Invalid number; enter a valid number")
        elif float(costStr) < 0:
            print("Price must be >= $0 \n Invalid input; enter a valid number")

        else:
            cost= float(costStr)
            break

    print(movieName+" ("+description+"), $"+str("%-0.2f" %(cost))+ " now available for hire")
    f = open("Items.csv", 'a')
    new = movieName+","+description+","+str(cost)+","+"in\n"
    f.write(new)
    f.close()


""" hireItems Function
function hireItems():
           open file ("items.csv",'r')
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


