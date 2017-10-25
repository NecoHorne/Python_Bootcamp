#Milestone Project 2 -
#Blackjack Game In this milestone project you will be creating a Complete BlackJack Card Game in Python.

import random

greeting = "Welcome to BlackJack"

class Player(object):
    """
    This Class will define the player in the black jack game, attributes and methods available to the player .
    """

    def __init__(self, name = 'name', bankroll=0.0):
        self.name = name
        self.bankroll = bankroll

    def bet(self,bet_amount):
        if bet_amount > self.bankroll:
            raise RuntimeError('Amount greater than available bankroll.')
        self.bankroll -= bet_amount
        return self.bankroll

    def win(self,winnings):
        self.bankroll += winnings
        return self.bankroll

def hash_string(keyword, bucket):
    position = []
    hash_ = 0
    for char in keyword:
        position.append(ord(char))
    for num in position:
        hash_ = hash_ + num
    return hash_ % bucket

def make_hashtable(nbuckets):
    hash_table = []
    for buckets in range(0,nbuckets):
            hash_table.append([])
    return hash_table

def hashtable_get_bucket(htable,keyword):
	return htable[hash_string(keyword, len(htable))]

def hashtable_add(htable, key, value):
	bucket = hashtable_get_bucket(htable,key)
	bucket.append([key,value])
	return htable

def hashtable_lookup(htable,key):
	bucket = hashtable_get_bucket(htable,key)
	for value in bucket:
		if value[0] == key:
			return value[1]
	return None

def hashtable_update(htable,key,value):
    #this function will be used to update the value of an ace from 11 to 1
	bucket = hashtable_get_bucket(htable,key)
	for entry in bucket:
		if entry[0] == key:
			entry[1] = value
			return htable
	bucket.append([key,value])
	return htable

def bet_():
    bet_amount = raw_input("what would you like to bet?")
    return int(bet_amount)

def innit_deck():
    deck = make_hashtable(4)
    hashtable_add(deck,'K_S', 10)
    hashtable_add(deck,'Q_S', 10)
    hashtable_add(deck,'J_S', 10)
    hashtable_add(deck,'10_S', 10)
    hashtable_add(deck,'9_S', 9)
    hashtable_add(deck,'8_S', 8)
    hashtable_add(deck,'7_S', 7)
    hashtable_add(deck,'6_S', 6)
    hashtable_add(deck,'5_S', 5)
    hashtable_add(deck,'4_S', 4)
    hashtable_add(deck,'3_S', 3)
    hashtable_add(deck,'2_S', 2)
    hashtable_add(deck,'A_S', 11)
    hashtable_add(deck,'K_D', 10)
    hashtable_add(deck,'Q_D', 10)
    hashtable_add(deck,'J_D', 10)
    hashtable_add(deck,'10_D', 10)
    hashtable_add(deck,'9_D', 9)
    hashtable_add(deck,'8_D', 8)
    hashtable_add(deck,'7_D', 7)
    hashtable_add(deck,'6_D', 6)
    hashtable_add(deck,'5_D', 5)
    hashtable_add(deck,'4_D', 4)
    hashtable_add(deck,'3_D', 3)
    hashtable_add(deck,'2_D', 2)
    hashtable_add(deck,'A_D', 11)
    hashtable_add(deck,'K_H', 10)
    hashtable_add(deck,'Q_H', 10)
    hashtable_add(deck,'J_H', 10)
    hashtable_add(deck,'10_H', 10)
    hashtable_add(deck,'9_H', 9)
    hashtable_add(deck,'8_H', 8)
    hashtable_add(deck,'7_H', 7)
    hashtable_add(deck,'6_H', 6)
    hashtable_add(deck,'5_H', 5)
    hashtable_add(deck,'4_H', 4)
    hashtable_add(deck,'3_H', 3)
    hashtable_add(deck,'2_H', 2)
    hashtable_add(deck,'A_H', 11)
    hashtable_add(deck,'K_C', 10)
    hashtable_add(deck,'Q_C', 10)
    hashtable_add(deck,'J_C', 10)
    hashtable_add(deck,'10_C', 10)
    hashtable_add(deck,'9_C', 9)
    hashtable_add(deck,'8_C', 8)
    hashtable_add(deck,'7_C', 7)
    hashtable_add(deck,'6_C', 6)
    hashtable_add(deck,'5_C', 5)
    hashtable_add(deck,'4_C', 4)
    hashtable_add(deck,'3_C', 3)
    hashtable_add(deck,'2_C', 2)
    hashtable_add(deck,'A_C', 11)
    return deck

def innit_deck_pull():
    deck_pull = ['A_S', '2_S', '3_S', '4_S', '5_S', '6_S', '7_S', '8_S', '9_S', '10_S', 'J_S', 'Q_S', 'K_S','A_C', '2_C', '3_C', '4_C', '5_C', '6_C', '7_C', '8_C', '9_C', '10_C', 'J_C', 'Q_C', 'K_C', 'A_H', '2_H', '3_H', '4_H', '5_H', '6_H', '7_H', '8_H', '9_H', '10_H', 'J_H', 'Q_H', 'K_H', 'A_D', '2_D', '3_D', '4_D', '5_D', '6_D', '7_D', '8_D', '9_D', '10_D', 'J_D', 'Q_D', 'K_D']
    return deck_pull

def innit_player():
    p_1 = raw_input('what is your name?')
    player = Player(name = p_1, bankroll = 500.0)
    return player

def player_cards(deck, deck_pull):
    random.shuffle(deck_pull)
    first_card = deck_pull[-1]
    deck_pull.pop(-1)
    second_card = deck_pull[-1]
    deck_pull.pop(-1)
    return [first_card, second_card]

def dealer_cards(deck , deck_pull):
        random.shuffle(deck_pull)
        first_card = deck_pull[-1]
        deck_pull.pop(-1)
        second_card = deck_pull[-1]
        deck_pull.pop(-1)
        return [first_card, second_card]

def hit_card(cards, deck, deck_pull):
    hit_card = deck_pull[-1]
    cards.append(hit_card)
    deck_pull.pop(-1)
    return cards

def hand_value(cards, deck):
    value = 0
    for card in cards:
        value = hashtable_lookup(deck,cards[cards.index(card)]) + value
    return value

def win_check(player_val, dealer_val):
    if player_val > 21:
        return "You Bust!"
    if player_val == 21:
         return "Congrats, you have 21!"
    if dealer_val > 21 and player_val < 21:
         return "The Dealer Busts!, You win"
    if dealer_val == 21:
        return "the Dealer has 21, you lose"
    if player_val < 21 and dealer_val < player_val:
        return "YOU WIN!"
    if dealer_val < 21 and player_val < dealer_val:
        return "YOU LOSE!"
    if dealer_val == player_val:
        return "its a tie"

def winning(player_val,dealer_val,player,bets):
    if player_val == 21:
        player.win(bets * 2)
    if dealer_val > 21 and player_val < 21:
        player.win(bets * 2)
    if player_val < 21 and dealer_val < player_val:
        player.win(bets * 2)
    if dealer_val == player_val:
        player.win(bets)

def innit_blackjack():
    #game Innit
    deck = innit_deck() #deck key value set
    deck_pull = innit_deck_pull() #deck from which cards will be drawn
    player = innit_player() #player created by player object class

    #game Greeting
    print str(greeting) + ' ' + str(player.name) + ", your bankroll is:", "$"+ str(player.bankroll) + " , GOOD LUCK!!"

    #main game loop
    while True:
        bets = bet_()
        player.bet(bets)

        print 'your current bankroll is:' + '$' + str(player.bankroll)

        #Draw procedure
        player_hand = player_cards(deck, deck_pull)
        player_h_val = hand_value(player_hand, deck)
        print 'your hand:' + str(player_hand) + "your hand's value is:" + str(player_h_val)

        dealer_hand = dealer_cards(deck,deck_pull)
        dealer_h_val = hand_value(dealer_hand, deck)
        print "The Dealer has:" + str(dealer_hand) + "The Dealer's hand value is:" + str(dealer_h_val)

        #Hit procedure

        player_hit = raw_input("would you like to hit? enter Y or N \n")
        if player_hit == 'Y' or player_hit == 'y':
            player_hand = hit_card(player_hand, deck, deck_pull)
            player_h_val = hand_value(player_hand, deck)
            print 'your hand:' + str(player_hand) + "your hand's value is:" + str(player_h_val)

        if dealer_h_val < 17 and dealer_h_val < player_h_val:
            print "The Dealer Hits!"
            dealer_hand = hit_card(dealer_hand,deck,deck_pull)
            dealer_h_val = hand_value(dealer_hand, deck)
            print "The Dealer has:" + str(dealer_hand) + "The Dealer's hand value is:" + str(dealer_h_val)

        print win_check(player_h_val, dealer_h_val)
        winning(player_h_val,dealer_h_val,player, bets)
        if player.bankroll <= 0:
            print "Sorry," + str(player.name) + "you are flat BROKE!!"
            break

innit_blackjack()
