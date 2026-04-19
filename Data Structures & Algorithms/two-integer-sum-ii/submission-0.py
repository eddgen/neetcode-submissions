class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num in numbers:
            num2 = target - num
            if num2!=num:
                if num2 in numbers:
                    return [numbers.index(num)+1,numbers.index(num2)+1]
            else:
                if numbers[numbers.index(num)+1] == num:
                    return [numbers.index(num)+1,numbers.index(num)+2]