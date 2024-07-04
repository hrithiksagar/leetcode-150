class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # a word char cant be repeated twice. 
        # Create a counter for the characters in 'chars'
        chars_count = Counter(chars)
        print("Char_count = ", chars_count)
        total_length = 0
        for word in words:
            word_count = Counter(word)
            print("word_count = ",word_count)
            # Check if word_count is a subset of chars_count
            if word_count & chars_count == word_count:
                total_length += len(word)
        
        return total_length