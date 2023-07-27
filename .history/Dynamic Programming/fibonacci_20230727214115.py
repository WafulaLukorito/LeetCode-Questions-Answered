

def fibonacci(n):
    
    #initialize array:
    arr= [0, 1] + [-1]*n
    
    for i in range (2, n+1):
        arr[i] = arr[i-2] + arr[i-1]
    
    return arr[n]