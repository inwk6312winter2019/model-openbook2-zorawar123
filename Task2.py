street1=[] # defining 2 list
Roads=[]
def func(): # Fuction
  file1=open('Street_Centrelines.csv',r) # Reading and opening both files
  file2=open('Bus_Stops.csv',r) 
    for i in file2:  
      i=i.strip()
      word1=sent.split(',') # seprating each word by strip and splitting by using ","
        if word1[7]=='Accessible': # Comparing the string with string 
	  if word1[6] not in street1: # again comapring the word 6 with street1 if its not there ,it will append in road
	    road=word1[6] # as the 6th word is not road, we will add word 6 in variable road
	      street1.append(road.lower()) # In the list we append the road in lower case letter
	else:
	  pass
	for j in file1:
	  j =j.strip()
	  word = j.split(',') # seprating each word by comma
	  if word2[10]=='ARTERIAL': # comapiring 10th word with given string
	    street2 =word2[2] # put the word in the 3rd position in street
	  if street2.lower() in street1: # comapiring the word in 3rd position with street
	    Roads.append(street)
	return(Roads)
print(func())
