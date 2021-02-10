"""
date:2/10/21
this will get all the possible ways in which a set can be ordered or arranged 
    
   example : abc = acb = bac = cab = cba = bca 
            
            
"""

from itertools import permutations


all_possible_outcome= permutations([1,2,4])


for i in list(all_possible_outcome):
    print(i)
    