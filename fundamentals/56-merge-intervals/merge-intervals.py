
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        result = []
        sorted_list = sorted(intervals)
        current = sorted_list[0].copy()

        for next_interval in sorted_list[1:]:
            if current[1] >= next_interval[0]:
                current[1] = max(current[1], next_interval[1])
            else:
                result.append(current)
                current = next_interval.copy()

        result.append(current)
        return result
