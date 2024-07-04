class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        print(paths)
        cities = set()
        for start,end in paths:
            cities.add(start)
            
        print(cities)
        print(end)
        
        
        for start,end in paths:
            if end not in cities:
                return end
            