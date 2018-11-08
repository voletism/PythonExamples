import os
import sys

def main():

    #arguments = sys.argv[1:][0]
    #print(arguments)

    # Tuples  ( tuples are immutable, you need to create a new tuple in order to achieve this)
    example = (1, 2, 3, "hello", "world" ,"movie")
    print(example[1:5])
    print(sys.getsizeof(example))

    # Lists
    lists_example = [2, 3, 4, "hello", "world", "movie"]
    print(lists_example[1:5])
    print(sys.getsizeof(lists_example))

    # list comprehensions
    list_squares = []
    for i in range(1,100):
        list_squares.append( i**2)
        print(list_squares)

    # also
    list_squares2 = [ i**2 for i in range (1 ,100)]
    print(list_squares2)

    # movies start with letter 'G'

    movies = ["Start wars", "Gandhi", "Megha", "Ghostbusters", "Temple",
              "Devadas", "Titanic", "Predator", "Skyfall", "Gattaca"]
    gmovies = []
    for title in movies:
        if title.startswith("G"):
            gmovies.append(title)
            print(gmovies)

    #alternatives
    globalmovies = [title for title in movies if title.startswith("G") ]
    print(globalmovies)

    moviesYear = [("Start wars", 1981), ("Gandhi",1984), ("Megha",2001), ("Ghostbusters",2014), ("Temple", 2018),
                  ("Devadas",2018), ("Titanic", 1997), ("Predator",1980), ("Skyfall",2015),
                  ("Gattaca", 1965)]

    y2kmovies = []
    for (title, year) in moviesYear:
        if year > 2000:
            y2kmovies.append((title,year))

    print(y2kmovies)

    ymovies = [ title for (title,year) in moviesYear if year > 2000]
    print(ymovies)

    w = [2, 3, -1]
    y = [2*x for x in w]
    print(y)

    #cartesian_product
    A =[1,3,5,7,9,11,13,15]
    B = [2,4,6,8,10,12,14]
    cartesian_product = [(a,b) for a in A for b in B]
    print(cartesian_product)

    return

if __name__ == "__main__":
    main()