word = "love"
length = len(word)
def string(a): 
    if length > 2 and a[-3:] == 'ing': # used sliceing method of string 
        a += 'ly'
    else:
        a += 'ing'
    return(a)
    
print(string('word'))
print(string('abcing')) 
  
