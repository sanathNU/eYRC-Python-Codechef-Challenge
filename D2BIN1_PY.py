''' Created for solving CodeChef Problem D2BIN1_PY
Problem Definition:
    Given a decimal number n, your task is to convert it to its binary equivalent using a recursive function.

    The code stub provided here is to be used. It calls the function dec_to_binary(). Your task is to complete the function.

    The binary number output must be of length 8 bits.
'''

'''
This script is code stub for CodeChef problem code D2BIN1_PY
Filename:      D2BIN1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''
def decbin(n,dig,ans):
    if(dig==0):
        return ans
    return decbin(n%dig,dig//2,ans+str(n//dig))

def dec_to_binary(n):
    bin_num = decbin(n,128,"")
    # Complete this function to return binary equivalent output of the given number 'n' in 8-bit format
    return bin_num

# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the n value
    for case in range(1,test_cases+1):
        # take the n input values
        n = int(input())

        # print (n)
        
        # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
        bin_num = dec_to_binary(n)
        print(bin_num)

