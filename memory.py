# implementation of card game - Memory

import simplegui
import random

WIDTH = 50
HEIGHT = 100
deck1, deck2 = range(8), range(8)
full_deck = deck1 + deck2
exposed = [False for i in range(16)]
card1 = 0
card2 = 0

# helper function to initialize globals
def new_game():
    global full_deck, state, exposed, moves
    random.shuffle(full_deck)
    exposed = [False for i in range(16)]
    state = 0
    moves = 0
           
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, full_deck, card1, card2, moves    
    for card in range(0,len(full_deck)):
        if pos[0] >= (50 * card) and pos[0] <= (50 * (card + 1)):
            print "index 'card': "+str(card)
            if exposed[card] == False:
                exposed[card] = True
    
                if state == 0:
                    state = 1
                    card1 = card
                    print "Frist card: ", full_deck[card1]
                elif state == 1:
                    state = 2
                    card2 = card
                    print "Second card: ", full_deck[card2]
                    moves += 1                
                else:
                    state = 1
                    if full_deck[card1] != full_deck[card2]:      
                        exposed[card1] = False
                        exposed[card2] = False
                    card1 = card
                    print "First card: ", full_deck[card1]
      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global full_deck, exposed, moves  
    for card in range(0,len(full_deck)):
        if exposed[card]:
            canvas.draw_text(str(full_deck[card]), [WIDTH*card+10,HEIGHT-25], 60, "White")            
        else:
            canvas.draw_polygon([((WIDTH*card),0), ((WIDTH*(card+1)),0), ((WIDTH*(card+1)),100), ((WIDTH*card),100)], 1, "Orange", "Green")
           
    label.set_text("Turns =" + str(moves))
      
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
