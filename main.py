import random
face = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

'''
This class defines each card in the deck.
'''
class Cards:
    def __init__(self,face,rank):
        self.face = face
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank+' of '+self.face
        
'''
This class defines the deck of card. 
'''
class Deck:
    def __init__(self):
        self.all_cards = []
        
        #CREATE THE DECK OF CARD
        for face in suits:
            for num in rank:
                self.all_cards.append(Cards(face,num))
    
    #SHUFFLE THE DECK
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    #TAKE OUT ONE CARD FROM THE DECK TO DISTRIBUTE AMONG THE PLAYERS
    def deal_one(self):
        return self.all_cards.pop()

'''
Class that define the player
'''
class Player:
    def __init__(self,name):
        self.name = name
        self.my_cards = [] #STORES THE CARDS FOR PERTICULAR PLAYER
        
    #TO DRAW OUT 1 CARD FROM THE CARDS    
    def remove_card(self):
        return self.my_cards.pop(0);
    
    #ADD THE CARDS TO PLAYERS STACK 
    def add_cards(self,cards):
        if type(cards) == type([]):
            self.my_cards.extend(cards)
        else:
            self.my_cards.append(cards)
    
    def __str__(self):
        return f'{self.name} has {len(self.my_cards)} cards'


#GAME SETUP
player1 = Player('One')
player2 = Player('Two')

deck = Deck()
deck.shuffle()

for x in range(26):
    player1.add_cards(deck.deal_one())
    player2.add_cards(deck.deal_one())
    
#GAME LOGIC
game_on = True
counter = 0

while game_on:
    counter += 1
    print(f'Round no {counter}')
    
    if len(player1.my_cards) == 0:
        print('Playre 1 has no cards left, playre 2 win!')
        game_on = False
        break
    if len(player2.my_cards) == 0:
        print('Playre 2 has no cards left, playre 1 win!')
        game_on = False
        break
        
    player1_cards = []
    player1_cards.append(player1.remove_card())
    
    player2_cards = []
    player2_cards.append(player2.remove_card())
    
    war = True
    while war:
        
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            war = False
        
        elif player2_cards[-1].value > player1_cards[-1].value:
            player2.add_cards(player2_cards)
            player2.add_cards(player1_cards)
            war = False
        
        else:
            print('WAR!!')
            if len(player1.my_cards) < 3:
                print('Player one is out of cards..')
                print('Playre two wins!!')
                game_on = False
                break
            
            elif len(player2.my_cards) <3:
                print('Player two is out of cards..')
                print('Playre one wins!!')
                game_on = False
                break
            
            else:
                for temp in range(3):
                    player1_cards.append(player1.remove_card())
                    player2_cards.append(player2.remove_card())
