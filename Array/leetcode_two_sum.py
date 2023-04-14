class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range (len(nums)-1):
            for j in range (1,len(nums)):
                if j == i:
                    continue
                else:
                    if nums[i]+nums[j]==target:
                        print([i,j])
            

L = Solution()
L.twoSum([2,5,11,5],10)
