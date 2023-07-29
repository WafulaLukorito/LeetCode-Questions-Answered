
def get_squares(nums):
    ans = [0]*len(nums)
    nums_sqr=[num*num for num in nums]
    
    i=0
    j=len(nums)-1
    p= len(nums)-1
    
    while i <= j:
        if nums_sqr[i] >= nums_sqr[j]:
            ans[p]=nums_sqr[i]
            p-=1
            i+=1
        else:
            ans[p]=nums_sqr[j]
            p-=1
            j-=1
    return ans