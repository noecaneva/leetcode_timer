from typing import List
from functools import reduce
from operator import xor
class Solution:
    def singleNumber_bool(self, nums: List[int]) -> int:
        bit_string = [False]*(3*10**4 +1)
        neg_string = [False]*(3*10**4 +1)
        for num in nums:
            if num >= 0:
                bit_string[num] = not bit_string[num]
            else:
                neg_string[-num] = not neg_string[-num]
        try:
            number = bit_string.index(True)
        except ValueError:
            number = -1*neg_string.index(True)
        return number

    def bitSwitch(self, number):
        if number == 0:
            return 1
        else:
            return 0

    def singleNumber_int(self, nums: List[int]) -> int:
        bit_string = [0]*(3*10**4 +1)
        neg_string = [0]*(3*10**4 +1)
        for num in nums:
            if num >= 0:
                bit_string[num] = self.bitSwitch(bit_string[num])
            else:
                neg_string[-num] = self.bitSwitch(neg_string[-num])
        try:
            number = bit_string.index(1)
        except ValueError:
            number = -1*neg_string.index(1)
        return number
    
    def charSwitch(self, number):
        if number == '0':
            return '1'
        else:
            return '0'

    def singleNumberChar(self, nums: List[int]) -> int:
        bit_string = ['0']*(3*10**4 +1)
        neg_string = ['0']*(3*10**4 +1)
        for num in nums:
            if num >= 0:
                bit_string[num] = self.charSwitch(bit_string[num])
            else:
                neg_string[-num] = self.charSwitch(neg_string[-num])
        try:
            number = int(bit_string.index('1'))
        except ValueError:
            number = int(-1*neg_string.index('1'))
        return number
    
    def singleNumber_if(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for num in nums:
            if num >= 0:
                pos = pos ^ num
            else:
                neg = neg ^ (-num)
        if pos == neg:
            return 0
        if pos != 0:
            return pos
        else:
            return neg

    def singleNumber_speed(self, nums: List[int]) -> int:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        return bitmask
    
    def singleNumber_reduce(self, nums: List[int]) -> int:
        return reduce(xor, nums)
    
    def singleNumber(self, nums: List[int]) -> int:
        bitmask = 0
        tot_numbers = 3*10**4 +1
        for num in nums:
            bitmask ^= (num + tot_numbers)
        return bitmask - tot_numbers


SOLUTIONS = {
    "bool flipping": Solution().singleNumber_bool,
    "int flipping": Solution().singleNumber_int,
    "char flipping": Solution().singleNumberChar,
    "bit flipping": Solution().singleNumber_if,
    "bit no if flipping": Solution().singleNumber,
    "bitmask": Solution().singleNumber_speed,
    "reduce xor": Solution().singleNumber_reduce,
}