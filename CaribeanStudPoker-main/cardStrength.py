from cards import *
from itertools import combinations
import copy

hand_strength = {1: 'Royal-flush', 2: 'Straight-flush', 3: 'Quads', 4: 'Fullhouse', 5: 'Flush', 6: 'Straight', 7: 'Threes', 8: 'Two-pair', 9: 'Pair', 10: 'Card-high'}

def winningHand(p1_hand, p2_hand):
    out1 = handStrength(p1_hand)
    out2 = handStrength(p2_hand)
    
    if out1 < out2: 
        return 1
    elif out1 > out2: 
        return 2
    else:
        return breakTie(out1, p1_hand, p2_hand)

def handQualifies(hand):
    ranks = sorted(hand.getRanks())[::-1]
    if (handStrength(hand) == 10 and (ranks[0] < 14 or ranks[1] < 13)): return False
    return True

def getHandStrength(hand):
    strength = handStrength(hand)
    return hand_strength[strength]

def breakTie(outcome, p1_hand, p2_hand):
    r1 = getRankCount(p1_hand)
    r2 = getRankCount(p2_hand)

    #if the outcome is either a fullhouse, quads or triples
    if outcome in [3,4,7]: 
        if max(r1, key=r1.get) > max(r2, key=r2.get): return 1
        return 2
    
    #if the outcome is a royal flush
    if outcome == 1:
        return 3
    
    #if the outcome is a straight-flush or straight
    if outcome in [2, 6]:
        h1 = max(r1.keys())
        h2 = max(r2.keys())

        if h1 == h2: return 3 #same straight
        if h1 > h2 and h1 != 14: return 1
        return 2

    #if the outcome is a flush or highcard
    if outcome in [5, 10]:
        r1_sorted = sorted(r1.keys())[::-1]
        r2_sorted = sorted(r2.keys())[::-1]

        while r1_sorted:
            if r1_sorted[0] > r2_sorted[0]: return 1
            if r1_sorted[0] < r2_sorted[0]: return 2
            else: 
                del r1_sorted[0]
                del r2_sorted[0]
        return 3

    #if the outcome is a two pair or a pair
    if outcome in [8,9]:
        pairs1 = sorted([i for i,j in r1.items() if j == max(r1.values())])[::-1]
        pairs2 = sorted([i for i,j in r2.items() if j == max(r2.values())])[::-1]
        
        single1 = sorted(list(rank for rank in set(r1.keys()) if rank not in pairs1))[::-1]
        single2 = sorted(list(rank for rank in set(r2.keys()) if rank not in pairs2))[::-1]
        
        while pairs1:
            if pairs1[0] > pairs2[0]: return 1
            if pairs1[0] < pairs2[0]: return 2
            else: 
                del pairs1[0]
                del pairs2[0]
        
        while single1:
            if single1[0] > single2[0]: return 1
            if single1[0] < single2[0]: return 2
            else: 
                del single2[0]
                del single2[0]

        return 3
        
    return -1

def handStrength(hand):
    #create dictionary with count of each rank
    rank_count = getRankCount(hand)
    ranks = rank_count.keys()

    #check for each possible outcome, starting from most valuable
    if royal_flush(hand, ranks): return 1
    if straight_flush(hand, ranks): return 2
    if quads(rank_count): return 3
    if fullHouse(rank_count): return 4
    if flush(hand): return 5
    if straight(ranks): return 6
    if threes(rank_count): return 7
    if twoPair(rank_count): return 8
    if pair(rank_count): return 9
    return 10

def bonus51(dealer_hand, player_hand):
    total_cards = copy.deepcopy(player_hand.getCards())
    total_cards.append(dealer_hand.getCards()[0])
    highest_strength = 10
    combo = combinations(total_cards, 5)

    for combination in combo:
        temp_hand = Hand([])
        temp_hand.createCustomHand(list(combination))
        strength = handStrength(temp_hand)
        if strength < highest_strength:
            highest_strength = strength
    return int(highest_strength)

def royal_flush(hand, ranks):
    if flush(hand) and set(ranks) == set((10,11,12,13,14)):
        return True
    return False

def straight_flush(hand, ranks):
    if flush(hand) and straight(ranks):
        return True
    return False

def quads(ranks_count):
    if sorted(ranks_count.values()) == [1,4]:
        return True
    return False

def fullHouse(ranks_count):
    if sorted(ranks_count.values()) == [2,3]:
        return True
    return False

def flush(hand):
    suit = hand.getCards()[0].getSuit()
    for card in hand.getCards():
        if card.getSuit() != suit:
            return False
    return True

def straight(ranks):
    if len(ranks) == 5 and max(ranks) - min(ranks) == 4:
        return True
    elif set(ranks) == set((2,3,4,5,14)):
        return True
    return False

def threes(ranks_count):
    if sorted(ranks_count.values()) == [1,1,3]:
        return True
    return False

def twoPair(ranks_count):
    if sorted(ranks_count.values()) == [1,2,2]:
        return True
    return False

def pair(ranks_count):
    if sorted(ranks_count.values()) == [1,1,1,2]:
        return True
    return False

def getRankCount(hand):
    rank_count = {}
    for card in hand.getCards():
        if card.getRank() not in rank_count:
            rank_count[card.getRank()] = 1
        else:
            rank_count[card.getRank()] += 1
    return rank_count


