class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {"N" : [0,1],
               "S" : [0, -1],
               "E" : [1,0],
               "W" : [-1,0]
        }
        visit = set({0,0}) # (x,y)
        x,y = 0, 0
        for c in path:
            visit.add((x,y))
            dx, dy = dir[c]
            x,y = x+dx, y+dy
            if (x,y) in visit:
                return True
        return False
        
    
        
        # if path=="NESW":
        #     return True
        # elif path=="NWSE":
        #     return True
        # elif path == "SENW":
        #     return True
        # elif path == "SWNE":
        #     return True
        # else:
        #     path = (i for i in path)
        #     for i in path:
            