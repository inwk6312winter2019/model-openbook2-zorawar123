class card(): # define the class
        s_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] # Cards name
        r_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King'] 
        def __init__(self,rank=0,suite=2): # Define init method which invoke aotomatically
                self.rank=rank # assisgning value by self
                self.suite=suite
        def __str__(self):
                return(f"The rank is {card.r_names[self.rank]} and the suit is {card.s_names[self.suite]}") # return the ace of sapde
spade=card(2,3)
print(spade)