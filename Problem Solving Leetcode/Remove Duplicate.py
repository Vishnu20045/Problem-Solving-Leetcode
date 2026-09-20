def removeDuplicates (nums):
        if not nums:
            return 0
        i=0
        for j in range(0,len(nums)):
            if nums[j]!=nums[i]:
                 i+=1
                 nums[i]=nums[j]
        return i+1
arr = [1,2,3,1]
print(removeDuplicates(arr))