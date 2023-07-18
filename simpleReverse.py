# Given a string A, you are asked to reverse the string and return the reversed string.
# Input:A = "scaler"
# Output:"relacs"

def simpleReverse(string):
    result=""
    for i in range(len(string)-1,-1,-1):
        result+=string[i]
    return result


string=input()
print(simpleReverse(string))