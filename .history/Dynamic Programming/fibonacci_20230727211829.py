

def fibonacci(n):
    arr = [0, 1] + [-1]*n
    
    for i in range (2, n+1):
        arr[n]=arr[n-2]+arr[n-1]
        
    return arr[n]