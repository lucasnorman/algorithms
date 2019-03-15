# Write a function to perform integer division without using either the / or * operators.

def division(dividend, divisor):
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    
    dividend = abs(dividend) 
    divisor = abs(divisor) 
    
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    
    return sign * quotient


print(division(15, 3)) # 5
