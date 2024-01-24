#define a function for exponent
def exponent(base, exp):
    #add variable number and result
    number = exp
    result = 1
    #while loop for number is greater than 0
    while number > 0:
        result = result * base
        number = number - 1
    #print result for the exponent
    print(base, "raises to the power of", exp, "is: ", result)
    
#checking if the function is working