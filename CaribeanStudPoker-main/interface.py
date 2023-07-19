import gui
import cardStrength as cards

# Payout Table
payout_table = {1: 100, 2: 50, 3: 20, 4: 7, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1, 10: 1}
bonus_payout_table = {1: 1000, 2: 200, 3: 100, 4: 20, 5: 15, 6: 10, 7: 7}

class CaribbeanStudPoker():
    def __init__(self):
        # Variables 
        self.current_cards = []
        self.dealer_hand = None
        self.player_hand = None
        self.log_index = 0
        self.money = 0

        self.app = gui.GUI()
        self.initializeButtons()
        self.app.updateMoneyLabel(self.money)
        self.app.mainloop()
        
    def initializeButtons(self):
        # Configure buttons
        self.app.getDealButton().configure(command=self.dealHand)
        self.app.getRebetButton().configure(command=self.rebet)
        self.app.getFoldButton().configure(command=self.fold)
        self.app.getUpdateMoneyButton().configure(command=self.updateMoney)
        self.app.getCashoutButton().configure(command=self.app.destroy)

        # Enable/Disable Valid buttons
        self.app.enableDealButton()
        self.app.disableRebetButton()
        self.app.disableFoldButton()

    def dealHand(self):    
        if (self.app.checkAnteValue() == False):
            self.app.insertLogMessage(self.log_index, f"Invalid Ante Bet          ")
            self.log_index += 1

        elif (self.app.check51BonusValue() == False):
            self.app.insertLogMessage(self.log_index, f"Invalid 5+1 bonus bet          ")
            self.log_index += 1

        elif ((int(self.money) - (int(3*self.app.getAnteValue()) + int(self.app.get51BonusValue()))) < 0):
            self.app.insertLogMessage(self.log_index, f"Insufficient funds. Deposit required to continue          ")
            self.log_index += 1
        else:
            ante_value = self.app.getAnteValue()
            bonus_value = self.app.get51BonusValue()

            # Disable Buttons 
            self.app.disableEntry()
            self.app.disableDealButton()
            self.app.disableUpdateMoneyButton()
            self.app.updateRaiseLabel('')

            # Deal Cards and update money
            self.current_cards = []
            self.dealer_hand = cards.Hand(self.current_cards)
            self.player_hand = cards.Hand(self.current_cards)   
            self.money = self.money - ante_value - bonus_value
            self.app.updateMoneyLabel(self.money)

            # Show cards
            self.app.resetCards()
            self.revealPlayerCards()
            self.revealDealerFirstCard()

            # Continue game
            self.app.enableRebetButton()
            self.app.enableFoldButton()

    def rebet(self):
        ante_value = self.app.getAnteValue()

        # Disable Buttons
        self.app.disableRebetButton()
        self.app.disableFoldButton()
        
        # Display Bet Value and update Money
        self.money = self.money - 2*ante_value
        self.app.updateRaiseLabel(ante_value*2)
        self.app.updateMoneyLabel(self.money)

        # Reveal Final Cards
        self.revealDealerCards()

        # Calculate Winner and update Money
        self.calculateWinner()

        # Reset Game
        self.resetGame()

    def fold(self):

        # Disable Buttons
        self.app.disableRebetButton()
        self.app.disableFoldButton()

        # Reveal Final Cards
        self.revealDealerCards()
        
        bonus_value = self.app.get51BonusValue()
        ante_value = self.app.getAnteValue()

        if bonus_value != 0:
            bonus_strength = cards.bonus51(self.dealer_hand, self.player_hand)
            if bonus_strength <= 7:
                bonus_payout = bonus_payout_table[bonus_strength]*bonus_value
                self.money = self.money + bonus_payout
                self.app.insertLogMessage(self.log_index, f"BONUS 5+1: You win {bonus_payout}$!          ")
            else:
                self.app.insertLogMessage(self.log_index, f"BONUS 5+1: Bet {bonus_value}$ did not payout.          ")
            
            self.log_index += 1

        # Display fold
        self.app.insertLogMessage(self.log_index, f"PAYOUT: Bet {ante_value}$ did not payout since player folded.          ")
        self.log_index += 1
        # Reset Game
        self.resetGame()

    def resetGame(self):
        # Enable Buttons
        self.app.enableDealButton()
        self.app.enableUpdateMoneyButton()
        self.app.enableEntry()

    def revealPlayerCards(self):
        cards = self.player_hand.getCards()
        for i, card in enumerate(cards):
            self.app.after(500, self.app.revealOneCard(card, i, 'player'))    

    def revealDealerCards(self):
        cards = self.dealer_hand.getCards()
        for i, card in enumerate(cards):
            self.app.after(500, self.app.revealOneCard(card, i, 'dealer'))  

    def revealDealerFirstCard(self):
        first_card = self.dealer_hand.getCards()[0]
        self.app.after(500, self.app.revealOneCard(first_card, 0, 'dealer')) 

    def calculateWinner(self):        
        ante_value = self.app.getAnteValue()
        bonus_value = self.app.get51BonusValue()

        if bonus_value != 0:
            bonus_strength = cards.bonus51(self.dealer_hand, self.player_hand)
            if bonus_strength <= 7:
                bonus_payout = bonus_payout_table[bonus_strength]*bonus_value
                self.money = self.money + bonus_payout
                self.app.insertLogMessage(self.log_index, f"BONUS 5+1: You win {bonus_payout}$!          ")
            else:
                self.app.insertLogMessage(self.log_index, f"BONUS 5+1: Bet {bonus_value}$ did not payout.          ")
            
            self.log_index += 1

        if (cards.handQualifies(self.dealer_hand) == False): #Dealer doesnt qualify
            self.money = self.money + (ante_value*3) + ante_value
            self.app.updateMoneyLabel(self.money)
            self.app.insertLogMessage(self.log_index, f"PAYOUT: You win {ante_value}$! Dealer did not qualify          ")
            
        elif (cards.winningHand(self.dealer_hand, self.player_hand) == 1): #Dealer wins hand
            self.app.insertLogMessage(self.log_index, f"PAYOUT: Bet {ante_value*3}$ did not payout. Dealers {cards.getHandStrength(self.dealer_hand)} beats Players {cards.getHandStrength(self.player_hand)}.          ")
        
        elif (cards.winningHand(self.dealer_hand, self.player_hand) == 3): #Tie
            self.app.insertLogMessage(self.log_index, f"PAYOUT: Bet {ante_value*3}$ is a push due to tie.          ")
            self.money = self.money + (ante_value*3)
        else:
            payout = payout_table[cards.handStrength(self.player_hand)]*(ante_value*2)
            self.money = self.money + (ante_value*3) + payout + ante_value
            self.app.updateMoneyLabel(self.money)
            self.app.insertLogMessage(self.log_index, f"PAYOUT: You win {payout}$! Players {cards.getHandStrength(self.player_hand)} beats Dealers {cards.getHandStrength(self.dealer_hand)}.          ")

        self.log_index += 1

    def updateMoney(self):
        value = self.app.getMoneyEntryValue()
        self.app.clearDepositEntry()

        if value != None:
            self.money += int(value)
            self.app.updateMoneyLabel(self.money)
            self.app.insertLogMessage(self.log_index, f"${value} has been deposited!          ")
            self.log_index += 1
        else:
            self.app.insertLogMessage(self.log_index, f"Invalid deposit.          ")
            self.log_index += 1

