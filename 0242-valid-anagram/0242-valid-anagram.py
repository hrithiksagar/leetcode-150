class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        hset1 = set()
        hset2 = set()

        for i in s:
            if i in hset1:
                None
            else:
                hset1.add(i)
                print("in S: ",hset1)

        for j in t:
            if j in hset2:
                None

            else:
                hset2.add(j)
                print("in T: ",hset2)
        print(hset1)
        print(hset2)

        for char in hset1:
            if s.count(char) != t.count(char):
                return False
        if hset1 == hset2:
            return True
        return False

    