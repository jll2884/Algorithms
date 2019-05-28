def insertion_sort(A):
    for i in range(1,len(A)):  # will start at second index all the way to the end of list
        for j in range(i-1,0,-1):  # starts at i-0, stop at index 0, step by -1=meaning we will move to the left
            if A[j]>A[j+1]:  # if item on right is smaller then swap places
                A[j],A[j+1]= A[j+1],A[j]  # swap places
            else:
                break

    print(A)

insertion_sort([1,4,2,9])

def faster_insertion(A):
    for i in range(1, len(A)):
        curNum = A[i]
        for j in range(i-1,0,-1):
            if A[j]>curNum:
                A[j+1]=A[j]
            else:
                A[j+1]=curNum
                break
                