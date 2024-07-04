
#? Demonstrating time and space complexity using sum of nums

nums = [1, 2, 3, 4, 5]
n = len(nums)

for i in range(n):
    sum = 0
    sum += nums[i]

print(sum) #? O(n) time complexity --LINEAR TIME 

print (n*(n+1)/2) #? O(1) time complexity --CONSANT TIME