def secondelement(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums[-2]

mylist=[4,5,6,10,9]
print(secondelement(mylist))