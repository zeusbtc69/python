n = 7
mid = (n//2) + 1
for i in range(1,n+1):
    for j in range(1, n+1):
        if(i == mid or j == mid):
            print('*',end=' ')
        elif(i >= 2 and i <= n-1) and (j >= 2 and j <= n-1):
            if(i == 2 or i == n-1):
                print('#', end=" ")
            else:
                print('*',end=' ')
        elif(i == 1 or i == n) and (j >= mid-(mid//2) and j <= mid+(mid//2) and (j < n-1 and j > 2)):
            print('#', end=" ")
        else:
            print(" ",end=" ")
    print()



