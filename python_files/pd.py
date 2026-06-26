def primeOrNot(n = []):
    for i in n: 
        if i in [0, 1]:
            continue 
        if i in [2,3]:
            print('prime')
            continue

        for j in range(2,i):
            if i % j == 0:
                print('not a prime')
                break
        else:
            print('prime')
            

nums = []
i = input('enter number (seperated by ' '(space)) : ')
nums = list(map(int, i.split(" ")))
print(nums)

primeOrNot(nums)
