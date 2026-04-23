def double(n: int) -> int:
    return n * 2

num = double(21)
print(num)

# Collection types

from typing import List

def average(nums: List[int]) -> float:
    total = sum(nums)
    count = len(nums)
    return total / count

print(average([1, 2, 3, 4])) # 2.5


## Scores
from typing import Dict

def get_total_marks(scorecard: Dict[str, int]) -> int:
    marks = list(scorecard.values())  # marks : List[int]
    return sum(marks)

scores = {'english': 84, 'maths': 92, 'history': 75}
print(get_total_marks(scores))  # 251
   