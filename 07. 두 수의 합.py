nums = [2,7,11,15]
target = 9

#풀이 1. 브루트 포스
def bruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j] == target):
                print(i,j)
                break
            else:
                continue

bruteForce(nums,target)

#풀이 2. in 활용법
def usingIn(nums, target):
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1:]: #시간 복잡도는 동일하지만 in 함수가 더 가볍고 빠름
            print(i, nums[i+1:].index(target- nums[i])+ (i+1))
        else : continue

usingIn(nums, target)

#플이 3. 첫 번째 수를 뺀 결과 키 조회

def twoSum(nums, target):
    nums_map ={}

    for i, num in enumerate(nums):
        nums_map[num] = i
        if target - num in nums_map and i != nums_map[target-num]:
            print("twoSum : "+str(i)+ " " + str(nums_map[target-num]))

twoSum(nums,target)


def usingTwoPoint(nums, target):
    left, right = 0, len(nums)-1
    while left != right:
        if nums[left] + nums[right]< target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [nums[left], nums[right]]

nums.sort()
print(usingTwoPoint(nums,target))


