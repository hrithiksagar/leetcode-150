class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = defaultdict(int)
        
        for word in words:
            for char in word:
                char_count[char] += 1
                
        for c in char_count:
            if char_count[c] % len(words):
                return False
        return True