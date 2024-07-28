arr=[]
solution=[]
number=int(input("Enter a size of array: "))
for i in range(number):
    num=int(input("Enter array element "))
    arr.append(num)
length=len(arr)
temp = arr[:]
k=int(input("Enter value of k: "))
for i in range(len(temp)):
         for j in range(i+1,len(temp)):
            if (temp[i] + temp[j]) % k == 0:
                solution.append(temp[i])
                solution.append(temp[j])
                temp.pop(j)
                break
arr = sorted(arr)
temp_solution = sorted(list(solution))
i=0
if temp_solution == arr:
    while (i<length):
        print(solution[i] , solution[i+1])
        i = i + 2
else:
    print("solution dosent exists ")