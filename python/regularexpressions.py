# find the patterns without RegEx

# some global variable holding function information

test = "362-789-7584"
# write isphonenumber function with arguments text
def isPhoneNumber(text):
    global test
    test = text 
    # check length of string
    if len(text) != 12 :
        return False 
    # check area code from index 0 to index 2
    for i in range(0,3): # upto 3 but not including 3
        if not text[i].isdecimal():  
            return False
    # check hyphen in string
    if text[3] != '-':
        return False
    # check area code from index 4 to index 6
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False 
    # check hyphen in string
    if text[7] != '-':
        return False
    # check for phone number form index 8 to index 11
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    #if return true print following
    return True

print(test + ' is a phone number:' )
print(isPhoneNumber('362-789-7584'))

print('Is \"agents of shield\" is a phone number:')
print(isPhoneNumber('agents of shield'))

    