class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        # OR has trailing zeros means result is even
        # This requires at least 2 even numbers
        even_count = sum(1 for x in nums if x % 2 == 0)
        return even_count >= 2