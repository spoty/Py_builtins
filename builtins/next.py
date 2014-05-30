M = [[1,2,3],      [4,5,6],      [7,8,9]]

G = (sum(row) for row in M) # create a generator of row sums next(G) # Run the
iteration protocol

 next(iterator[,default])

    Retrieve the next item from the iterator by calling its next() method. If
    default is given, it is returned if the iterator is exhausted, otherwise
    StopIteration is raised.
