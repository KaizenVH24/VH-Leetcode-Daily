# Brute Force
class Solution:
    def minPartitions(self, n: str) -> int:
        digits = list(map(int, n))
        operations = 0

        while any(digits):
            for i in range(len(digits)):
                if digits[i] > 0:
                    digits[i] -= 1
            operations += 1

        return operations

# Optimized
class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 0
        for ch in n:
            max_digit = max(max_digit, int(ch))
        return max_digit

# Most Optimized
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
