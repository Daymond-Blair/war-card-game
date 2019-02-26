from random import shuffle

# create cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("Creating ordered deck of cards!")
        self.create_deck = [(s, r) for s in SUITE for r in RANKS]

    def cut_deck(self):
        print("Cutting cards!")
        return (self.create_deck[:26], self.create_deck[26:])

    def shuffle_deck(self):
        print("Shuffling deck!")
        return shuffle(self.create_deck)


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def draw_cards(self, new_cards):
        self.cards.extend(new_cards)

    def discard_cards(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_cards(self):
        drawn_card = self.hand.discard_cards()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []

        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.discard_cards())
            return war_cards

    def check_cards(self):
        '''
        Return true if player still has cards left
        '''
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

#[x] instantiate deck
#[x] instantiate player one object from player
#[x] instantiate computer object from player
#[x] create turn control for back and forth between player and computer
#[x] create win condition


deck = Deck()
deck.shuffle_deck()

# unpack split deck tuple
player_one_hand, player_two_hand = deck.cut_deck()

player_one = Player('Daymond', Hand(player_one_hand))
war_bot = Player('WarBot', Hand(player_two_hand))

player_one.check_cards()

total_rounds = 0
war_count = 0

while(player_one.check_cards() and war_bot.check_cards()):
    total_rounds += 1
    print("New round start!")
    print("Current standings:")
    print(player_one.name + " has " + str(len(player_one.hand.cards)))
    print(war_bot.name + " has " + str(len(war_bot.hand.cards)))

    print("Play a card!")
    print('\n')

    table_cards = []

    war_bot_card = war_bot.play_cards()
    player_one_card = player_one.play_cards()

    table_cards.append(war_bot_card)
    table_cards.append(player_one_card)

    if(player_one_card[1] == war_bot_card[1]):
        war_count += 1

        print('War!!!!')

        # grab war cards for each player
        table_cards.extend(player_one.remove_war_cards())
        table_cards.extend(war_bot.remove_war_cards())

        if RANKS.index(war_bot_card[1]) < RANKS.index(player_one_card[1]):
            player_one.hand.draw_cards(table_cards)
        else:
            war_bot.hand.draw_cards(table_cards)

        # TODO implement double-war scenario logic

    else:
        if RANKS.index(war_bot_card[1]) < RANKS.index(player_one_card[1]):
            player_one.hand.draw_cards(table_cards)
        else:
            war_bot.hand.draw_cards(table_cards)

print("Game over! Number of Rounds: " + str(total_rounds))
print("War happened " + str(war_count) + " times.")

print("Does the player still have cards? ")
print(str(player_one.check_cards()))

print("Doeos the bot still have cards? ")
print(str(war_bot.check_cards))
