def binarysearch(arr, low, high, x, columns):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            row = mid // columns
            col = mid % columns
            return [row, col]
        elif arr[mid] > x:
            return binarysearch(arr, low, mid - 1, x, columns)
        else:
            return binarysearch(arr, mid + 1, high, x, columns)
    else:
        return -1

def checknum(num1,col):
    if(num1 > col):
        return num1
    else:
        num1 = int(input("Enter a greater element than previous one: "))
        return checknum(num1,col)
rows=int(input("enter the no of rows: "))
columns=int(input("Enter the no of colums: "))
arr = []
for i in range(rows):
    row=[]
    for j in range(columns):
        print(i," ",j)
        num=int(input("Enter the element "))
        if j==0 and i==0:
            row.append(num)
        elif j==0 and i>0:
            num=checknum(num,arr[i-1][columns-1])
            row.append(num)
        else:
            num = checknum(num, row[j - 1])
            row.append(num)
    arr.append(row)
print(arr)
x = int(input("Serach an element: "))
single_arr=[]
for i in range(rows):
     for j in range(columns):
         num = arr[i][j]
         single_arr.append(num)
result = binarysearch(single_arr,0,len(single_arr)-1,x,columns)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")