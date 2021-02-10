"""
date:2/10/21
function  that will get the factorial of a particular given number
    
   example : 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 
              3! = 3 * 2 * 1 
            
            
!  this symbol represent factorial 
"""
def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(12))
              
    