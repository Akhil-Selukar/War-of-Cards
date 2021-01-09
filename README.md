# War-of-Cards

Game description:
Two players will start the game with half the deck each, then each player will draw a card, compare which card has the highest value, and the player with the higher card wins both cards. In case both the player has card of same value, it will be the war condition. In this case both player will draw 3 cards each and compare the value of 3rd drawn card and the player with greater value card will win all the cards. This process goes on until either one player loses all his cards or in case of war the playre is having less that 3 cards to play the war. The playre who wins all the card will be the winner.

Variables:
face : Global variable which holds all faces of cards that is Hearts, Diamonds, Spades and Clubs.
rank : the value of card, that might be ace, 2, 3, ..., jack, queen, king. 
values : it is a dictionary which have value assigned to each rank i.e. 2 for '2', 11 for 'jack', etc.

Classes:
Card : this class define each card in the deck.
Deck : This class defines the deck of card. 
Player : Class that define the player

Methods:
shuffle(self) : To shuffle the deck of cards.
deal_one(self) : To pick one cared from the deck.
remove_card(self) : Remove one card from the playres stack of card and return it.
add_cards(self,cards) : This method add one or more cards won by the playre to playres stack of creds.

