class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        """
        Given only valid emails. 
having a . in email is same as without . : Can be ignored
        having a + the next part of this can be ignored
        return number of unique emails
        can use hashsets

        """
        # unique = set()
        # for e in emails:
        #     local, domain = e.split("@") # splitting it to 2 strings
        #     local = local.split("+")[0]
        #     local = local.replace(".","")

        #     unique.add((local, domain))
        
        # return len(unique)


        # without using inbuilt function

        unique = set()
        for e in emails:
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i+=1
            while e[i] != "@":
                i+=1
            domain = e[i+1:]
            unique.add((local, domain))        
        return len(unique)

