cube = lambda x:x**3
 # complete the lambda function 

def fibonacci(n):
    lst=[0,1]
    for i in range(2,n):
        lst.append(lst[i-2]+lst[i-1])
    return lst[0:n]
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))