import fileinput

for line in fileinput.input():
    
    #declaring variables needed for each input string
    InputString = line.rstrip()
    Alpha = [0] * 26
    Beauty = 0
    
    #this is basically counting how many times each letter occurs and storing it in our
    #Alpha array 
    for i in InputString:
        if i.isalpha():
            Alpha[ord(i.lower()) - 97] += 1
    
    #sorting the array so we can traverse through it and multiply each by their
    #corresponding beauty value
    Alpha.sort()
    
    
    for i in range(25, -1, -1):
        #if that character is accounted for in the string break to the next value
        if Alpha[i] == 0:
            break
        #otherwise we will add the product of the Beauty value i+1 to the represented spot
        #in Alpha[i]
        Beauty += (i+1) * Alpha[i]
    
    #print the strings Beauty Value
    print Beauty