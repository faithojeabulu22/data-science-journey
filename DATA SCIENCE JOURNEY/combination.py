"""
date:2/10/21
function : this will determine the number of possible arrangements of items
    

            
"""

from itertools import combinations

all_posssible_arrangement = combinations([1,2,3,4],2)


for i in list(all_posssible_arrangement):
    print(i)
    