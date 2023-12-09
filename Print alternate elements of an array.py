#User function Template for python3

# arr is the array
# n is the number of elements in array
def printAl(arr,n):
    # your code here
    for i in range(len(arr)):
        if i==0 or i%2==0:
            print(arr[i],end=" ")
    return 0