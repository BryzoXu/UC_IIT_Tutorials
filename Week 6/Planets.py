Planets = [('Mercury', 75, 1), ('Venus', 460, 2), ('Mars', 140, 4), ('Earth', 510, 3), ('Jupiter', 62000, 5), ('Neptune', 7640, 8), ('Saturn', 42700, 6 ), ('Uranus',8100, 7)] 

def sort():
   return sorted(Planets, key=lambda p: p[1])
    
print(sort())