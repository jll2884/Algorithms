def bubble_sort(A):
    for i in range(0,len(A)-1): #loops through the whole array
        for j in range(0, len(A) - 1-i): #repeats through all items for every index
            if A[j]> A[j+1]: #checks to see if left side is bigger than right side
                A[j],A[j+1]= A[j+1],A[j]

    print(A)

bubble_sort(['a','c','b'])