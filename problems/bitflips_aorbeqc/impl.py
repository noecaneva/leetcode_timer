from typing import List

class Solution:
    def minFlips(self, inp: List[int]) -> int:
        a, b, c = inp
        # Mask on where bits have to be flipped
        or_xor_mask = (a | b)^c
        # in case that c is 0 and (a=b=1) it we have to do 2 flips so 
        # we add that case to the count
        and_mask = (a & b) & (~c)

        return or_xor_mask.bit_count() + and_mask.bit_count()
    
    def minFlips__(self, inp: List[int]) -> int:
        a, b, c = inp
        return ((a | b) ^ c).bit_count() + ((a & b) & ~c).bit_count()

SOLUTIONS = {
    "extended": Solution().minFlips,
    "concise": Solution().minFlips__,
}