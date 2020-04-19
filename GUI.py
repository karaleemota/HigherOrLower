#a GUI made using tkinter
# from tkinter import *
from Card import *
import tkinter as tk

#create instance----------------------------------------------------
window = tk.Tk()
window.geometry("1080x720") #make dimensions of gui
window.title("Higher or Lower")

#function that creates deck, iterates thru deck and assigns each card a button/image
def createDeck():
    deck = Deck()
    print(len(deck.cards))
    counter=0
    x = 0 #x coordinate of where card will be placed
    y = 0 #y coordinate of where card will be placed
    for card in deck.cards:#iterate thru the cards in the deck created
        #set the image and button ot card
        try: #catch the possible error of file not existing
            imageFile = getImage(card.suit,card.value)#the name of the image file png
        except: #if error occurs, do this
            imageFile = "images/red_joker.png"
        pic = tk.PhotoImage(file=imageFile).subsample(7)  # retrieve image
        print("in created decksss")
        print(card.suit)
        print(card.value)
        card.button = tk.Button(window, image=pic, command=lambda deckk=deck,cardd=card: cardClickedEvent(deckk, cardd))
        # card.image = pic #keep a reference to the image so garbage collection doesnt get it
        # card.button.command= lambda:deck.removeCard(card.suit,card.value)#remove the card from deck
        card.button.image = pic #save reference to image so it doesnt delete itself
        card.button.grid(row=x, column=y)#display the button on the screen
        #adjust grid layout for next card
        y += 1
        if(y % 13 == 0):
            x+=1
            y=0
    return deck

def cardClickedEvent(deck_, card_):#this event should happen when a card is clicked
    deck.removeCard(card_.suit, card_.value)
    probsOfHigher(card_,deck_)
    probsOfLower(card_,deck_)

#function that takes the suit name and vallue of card to find the right image name to use
def getImage(suit_, value_):
    value = value_ #this will hold a string of the value of the card
    suit = suit_#this will hold a string of the suit of the card
    if value_ >= 2 and value <= 10:#card is a numeric value
        value = value_
    elif value == 1: #ace
        value = "ace"
    elif value == 11:#jack
        value = "jack"
    elif value == 12:#Queen
        value = "queen"
    elif value == 13:#king
        value = "king"
    imageName = "images/" + str(value) + "_of_" + str(suit_) + ".png"
    print(imageName)
    return imageName

#function, given a deck and current card being played, says the probabilty the next card chosen is higher than the current card
def probsOfHigher(card, deck):
    highercnt = 0 #keep track of how many cards in deck have a higher rank than current card
    lowercnt = 0
    for othercard in deck.cards:
        if card.__ge__(othercard):
            lowercnt += 1
        else:
            highercnt += 1
    print("probabillity of higher next: " + str(highercnt / (highercnt + lowercnt)))
    return highercnt / (highercnt + lowercnt)

#function, given a deck and current card being played, says the probabilty the next card chosen is lower than the current card
def probsOfLower(card, deck):
    highercnt = 0  # keep track of how many cards in deck have a higher rank than current card
    lowercnt = 0
    for othercard in deck.cards:
        if card.__ge__(othercard):
            lowercnt += 1
        else:
            highercnt += 1
    print("probabillity of lower next: " + str(lowercnt / (highercnt + lowercnt)))
    return lowercnt / (highercnt + lowercnt)

#each card should contain a button that has a card image assigned to it
class Card:
    button = tk.Button(window)
    def __init__(self,suit,val):#initialize
        self.suit = suit
        self.value = val
    def __ge__(self,other):#override >= comparitor to see which card is ranked higher
        if(self.value > other.value):
            return True
        elif(self.value < other.value):
            return False
        else: # cards have same value, so compare suit. clubs > spades > diamonds > hearts
            thisSuit = 4 #use numbers to rank the suits
            otherSuit = 1
            if(self.suit == "clubs"):
                thisSuit = 1
            elif(self.suit == "spades"):
                thisSuit = 2
            elif(self.suit == "diamonds"):
                thisSuit = 4
            if(other.suit == "spades"):
                otherSuit = 2
            elif(other.suit == "diamonds"):
                otherSuit = 3
            elif(other.suit == "hearts"):
                otherSuit = 4
            #now compare suits
            if(thisSuit > otherSuit):
                return True
            else:
                return False

#class that repreents a single deck of 52 cards
#GAME RULES: in this game the order of ranking is(ascending): clubs, spades, diamonds, hearts
class Deck:
    cards = []
    def removeCard(self, cardSuit, cardValue):#remove a card from this deck
        print("in remove card")
        print("value "+str(cardValue)+"suit "+str(cardSuit))
        print(len(self.cards))
        for i, o in enumerate(self.cards):
            if o.value == cardValue and o.suit == cardSuit:
                # now we have to delete the card from the deck in the gui
                o.button.destroy()
                del self.cards[i]#delete card from deck
                break
    def createDeck(self):
        for suit in ["clubs","spades","diamonds","hearts"]:
            for value in range(1,14):#1=ace 11=jack 12=queen 13=king
                #assign the image to the card, and a button
                newCard = Card(suit,value)
                print(suit)
                print(value)
                self.cards.append(newCard)
        print("finished creating deck")

    def __init__(self):
        print("in deck inti")
        self.cards = [] # make an array of cards
        self.createDeck() #create the deck of cards

#call create deck to make the cards appear on the screen
print("create deck")
deck = createDeck()
#make window loop so it doens't close right away
window.mainloop()