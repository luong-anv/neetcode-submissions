class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        two, one = max(nums[1], nums[0]), nums[0]

        for i in range(2, len(nums)):

            tmp = max(nums[i]+one, two)
            one = two
            two = tmp

        return two


        