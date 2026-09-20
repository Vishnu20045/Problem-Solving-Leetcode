def elementsorted(nums):
    n = len(nums)-1
    for i in range(n):
        if nums[i]>nums[i+1]:
            return False
    return True
myarr=[1,2,3,4]
print(elementsorted(myarr))