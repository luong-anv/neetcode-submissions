class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        for integer in nums:
            hash[integer] += 1
        num_freq = [(v, num) for num, v in hash.items()]
        sorted_freq = sorted(num_freq, reverse=True)
        return [num for _, num in sorted_freq[:k]]