class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
#         we need 2 hashmaps to map word with pattern and map pattern with word. because one word cant me mapped to different patterns.

        words = s.split(" ")
        if len(pattern) != len(words): # base case
            return False
        
        #initializing 2 hashmaps
        char2word = {}
        word2char = {}
        
        for c,w in zip(pattern, words): # for characters in patterns are getting zipped with words in list. 
            # check if we have to return flase for any base case, 
            # if this character is already mapped to a word and also the word it mapps to isnnot equal to this word that we are curentrly looking at then its false
            if c in char2word and char2word[c] != w:
                return False
            # similarly
            if w in word2char and word2char[w] != c:
                return False
            # now if we reqch here, that means we are all sorted to find solution, we can add these 2 hashmaps
            char2word[c] = w
            word2char[w] = c
        return True
            
            
            
            
            
    
    
        