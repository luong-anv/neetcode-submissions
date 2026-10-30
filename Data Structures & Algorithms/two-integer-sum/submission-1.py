class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i in range(len(nums)):
            diff = target - nums[i]

            if nums[i] in hash:
                return [hash[nums[i]], i ]
            else:
                hash[diff] = i


        