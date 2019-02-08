fout = open('Street_Centrelines.csv','r') #It will open and perform read operation in file StreetCenterlines.csv

def tuple_func():
    for i in fout:
        i = i.split(",")
        string = (i[2],i[4],i[6],i[7]) # A tuple of (STR_NAME,FULL_NAME,FROM_STR,TO_STR)
        print(string)  
tuple_func()
