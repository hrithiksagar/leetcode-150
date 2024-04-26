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
        - May have one more more "." and "+"
        - After "@" its domain name
        - Beforee "@" its local name
        - having "." in local name will redirect to same local name
        - if "+" in local name, everything after that will be ignored - Not in DOMAIN NAM
        - 

        """
        a = set()
        for eachemail in emails:
            first, last = eachemail.split("@")
            # print(first)
            # print(last)
            """
            First = 
            test.email+alex
            leetcode.com
            test.e.mail+bob.cathy
            
            Last = 
            leetcode.com
            testemail+david
            lee.tcode.com
            now we need to modify first and last seperately
            
            """
            
            #modifying First part
            # if we see +, we ignore all after that
            if "+" in first:
                first = first[:first.index("+")]
            
            #replacing "." with nothing
            first = first.replace(".", "")
            
            #now add first to hashset
            a.add(first + "@" + last)
        return len(a)
            
            
            
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # unique = set()
        # for e in emails:
        #     local, domain = e.split("@") # splitting it to 2 strings
        #     local = local.split("+")[0]
        #     local = local.replace(".","")

        #     unique.add((local, domain))
        
        # return len(unique)


        # without using inbuilt function

#         unique = set()
#         for e in emails:
#             i, local = 0, ""
#             while e[i] not in ["@", "+"]:
#                 if e[i] != ".":
#                     local += e[i]
#                 i+=1
#             while e[i] != "@":
#                 i+=1
#             domain = e[i+1:]
#             unique.add((local, domain))        
#         return len(unique)

