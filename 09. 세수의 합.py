nums = [-1, 0, 1, 2, -1, -1, -4]

#01. 브루트 포스
def threeSum(nums : list ) -> list :
    ansList = []
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1] : continue
        for j in range(i+1, len(nums)-1):
            if j>i+1 and nums[j] == nums[j-1] : continue
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1] : continue
                if nums[i] + nums[j] + nums[k] == 0 :
                    ansList.append([nums[i],nums[j], nums[k]])
    return ansList

print(threeSum(nums))

def threeSumwithOutDuplicate(nums : list ) -> list :
    ansList = []
    nums.sort()
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 :
                    ansList.append([nums[i],nums[j], nums[k]])
    return ansList

print(threeSumwithOutDuplicate(nums))

#02. 투 포인터 합 계산

def twoPointSum(nums : list) -> list:
    ansList =[]
    nums.sort()

    for i in range(len(nums)-2) :
        if i> 0 and nums[i] == nums[i-1] : continue
        left, right = i+1, len(nums) -1
        while left < right:

            sum = nums[i] + nums[left] + nums[right]

            if sum < 0 :
                left +=1
            elif sum >0 :
                right -= 1
            else :
                print(i,left, right)
                ansList.append([nums[i], nums[left], nums[right]])

                if nums[left] == nums[left + 1]:
                    left += 1
                if nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return ansList

print(twoPointSum(nums))

