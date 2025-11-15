class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = {}
        res = ""
        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        #Add the character if it's present in hashmap to res
        for char in order:
            if char in hashmap:
                res += char * hashmap[char]
                del hashmap[char]
        #Add the remaining characters
        for char, count in hashmap.items():
            res += char * count
        return res