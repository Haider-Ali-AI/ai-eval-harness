class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = {}

        for word in strs:
            key = tuple(sorted(word))
            if key not in group :
                group[key] = []
            group[key].append(word)

        return list(group.values())