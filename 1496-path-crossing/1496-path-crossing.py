class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # # solution 1
        x,y = 0,0
        visited = set()
        visited.add((x,y))
        
        for dir in path:
            if dir == "N":
                y+=1
            elif dir == "S":
                y-=1
            elif dir == "E":
                x+=1
            elif dir == "W":
                x-=1
            if (x,y) in visited:
                return True
            visited.add((x,y))
        return False
        
        # # Solution 2
        # dir = {"N" : [0,1],
        #        "S" : [0, -1],
        #        "E" : [1,0],
        #        "W" : [-1,0]
        # }
        # visit = set({0,0}) # (x,y)
        # x,y = 0, 0
        # for c in path:
        #     visit.add((x,y))
        #     dx, dy = dir[c]
        #     print("loop ",{c}, "dx = ",dx,"dy = ",dy)
        #     print("x: ",x,"y: ",y)
        #     x,y = x+dx, y+dy
        #     print("x+dx: ",x,"y+dy: ",y)
        #     if (x,y) in visit:
        #         return True
        # return False
        
    
        
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
            