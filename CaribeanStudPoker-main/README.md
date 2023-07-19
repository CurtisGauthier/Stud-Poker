# CaribbeanStudPoker
A simple implementation of the popular casino game Caribbean Stud Poker

Running instruction: Download repository and run app.py
### Rules
1. Player makes an ante wager plus an optional 5+1 bonus side bet
2. Each player and the dealer get five cards each. All cards are dealt face down, except one dealer card is exposed. The player may examine his own cards but sharing of information is not allowed.
3. Player must fold or raise.
4. If player folds he forfeits his cards and ante bet.
5. If player raises then he must make a raise wager exactly equal to twice the ante
6. The dealer will turn over his other four cards
7. The dealer must have an ace and a king or higher to qualify. In other words, the lowest qualifying hand would be ace, king, 4, 3, 2 and the highest non-qualifying hand would be ace, queen, jack, 10, 9. If the dealer does not qualify the player will win even money on his ante wager and the raise will push.
9. If the dealer qualifies and beats the player, both ante and raise will lose.
10. If the dealer qualifies and loses to the player, then the ante will pay even money and the raise according to the posted pay table.
11. If the player and dealer tie, both ante and raise will push.

### Payout Table
1. Royal flush	100 to 1
2. Straight flush	50 to 1
3. Four of a kind	20 to 1
4. Full house	7 to 1
5. Flush	5 to 1
6. Straight	4 to 1
7. Three of a kind	3 to 1
8. Two pair	2 to 1
9. All other	1 to 1

### 5+1 Bonus rules
If you place the 5+1 Bonus side bet you win if your five cards plus the dealer’s first face up card make a five-card poker hand of a Three of a Kind or better

### 5+1 Bonus payout
1. Royal Flush	1,000 to 1
2. Straight Flush	200 to 1
3. Four of a Kind	100 to 1
4. Full House	20 to 1
5. Flush	15 to 1
6. Straight	10 to 1
7. Three of a Kind	7 to 1
