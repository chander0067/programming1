"""Name Chander deep
There two function below
1. first is the list of all movies and
2. The other function is to hire the movies or items which are available
 which are available for hiring
Git hub link
https://github.com/chander0067/programming1.git
"""
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
