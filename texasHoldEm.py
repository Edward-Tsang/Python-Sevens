import random
import sys

faces = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
suits = {"S": "Spades", "H": "Hearts", "C": "Clubs", "D": "Diamonds"}
deck = []
hands = [[]]

def generate_deck():
    for suit in suits.keys():
        for face in faces:
            deck.append(suit + face)
    random.shuffle(deck)


def get_num_of_players():
    numofPlayers = 0
    while numofPlayers < 1:
        try:
            numofPlayers = int(input("Please enter the number of players: "))
        except:
            print("Invalid number of players. Please try again")
        if numofPlayers < 1:
            print("There must be at least one other player.")
    return numofPlayers


def setupHands(numofPlayers):
    for player in range(numofPlayers):
        hands.append([])
    return hands


def deal_card(player, numofCards, hands):
    for card in range(numofCards):
        if player == "players":
            for playerCounter in range(len(hands) - 1):
                dealtCard = deck.pop()
                hands[playerCounter].append(dealtCard)
        elif player == "middle":
            dealtCard = deck.pop()
            hands[-1].append(dealtCard)
            print("The community cards are: ", end="")
            print(hands[-1])


def getUserInput():
    userInput = ""
    try:
        while userInput not in ["q", "c"]:
            userInput = input("Please press \"c\" to continue or \"q\" to fold: ")
    except ValueError:
        print("Invalid input. Please try again")
    if userInput == "q":
        print("User has forfeited the game.")
        sys.exit()


def getCardsList(hands):
    cardsList = []
    for hand in range(len(hands) - 1):
        cardsList.append([])
        cardsList[hand].extend(hands[hand])
        cardsList[hand].extend(hands[-1])
        cardsList[hand].sort()
    return cardsList


def checkforSameCards(cardsList):
    cardCount = {}
    pairValue = []
    maxPairValue = []
    for counter in range(len(cardsList)):
        pairValue.append([])
        maxPairValue.append([])
        cardCount[counter] = {}
        for hand in range(len(cardsList[counter])):
            playerHand = cardsList[counter]
            if playerHand[hand][1:] not in cardCount[counter]:
                cardCount[counter][playerHand[hand][1:]] = 1
            else:
                lastCount = cardCount[counter][playerHand[hand][1:]]
                cardCount[counter][playerHand[hand][1:]] = lastCount + 1
                if playerHand[hand][1:] not in pairValue[counter]:
                    pairValue[counter].append(playerHand[hand][1:])
    for pair in range(len(pairValue)):
        if pairValue[pair] != []:
            maxPairValue[pair] = max(pairValue[pair])
    return cardCount, maxPairValue


def checkforStraight(cardsList):
    straight = []
    faces = cardListtoFaces(cardsList)
    for hand in range(len(cardsList)):
        straight.append(1)
        faces[hand].sort()
        for face in range(len(faces[hand])):
            if face == 0:
                continue
            else:
                currentFace = faces[hand][face]
                if currentFace != int(faces[hand][face - 1]) + 1:
                    straight[hand] = 0
    return straight


def cardListtoFaces(cardsList):
    faces = []
    for counter in range(len(cardsList)):
        faces.append([])
        for hand in range(len(cardsList[counter])):
            faces[counter].append(convNametoNum(cardsList[counter][hand][1:]))
    return faces


def getHighestCard(cardsList):
    highestCards = []
    hasHighestCard = []
    faces = cardListtoFaces(cardsList)
    for counter in range(len(faces)):
        faces[counter].sort()
        highestCards.append(faces[counter].pop())
    highestCard = highestCards[0]
    hasHighestCard.append(0)
    for card in range(1, len(highestCards)):
        if highestCards[card] > highestCard:
            hasHighestCard.clear()
            highestCard = highestCards[card]
            hasHighestCard.append(card)
        elif highestCards[card] == highestCard:
            hasHighestCard.append(card)
    return hasHighestCard


def convNametoNum(face):
    if face == "A":
        face = 1
    if face == "J":
        face = 11
    if face == "Q":
        face = 12
    if face == "K":
        face = 13
    return int(face)


def checkforSameSuit(cards):
    suit = cards[0][0:1]
    for card in range(1, len(cards)):
        if cards[card][0:1] == suit:
            continue
        else:
            return 0
    return 1


def findMaxValue(listOfValues, listOfHands):
    maxValue = 0
    hasMaxValue = []
    for counter in range(len(listOfValues)):
        if int(listOfValues[counter]) > maxValue:
            hasMaxValue.clear()
            maxValue = int(listOfValues[counter])
            hasMaxValue.append(listOfHands[counter])
        elif int(listOfValues[counter]) == maxValue:
            hasMaxValue.append(listOfHands[counter])
    return hasMaxValue


def determineWinner(score, maxPairValue):
    players = []
    scores = []
    maxScore = 0
    hasMaxScore = []
    largestPair = 0
    hasLargestPair = []
    players.extend(score.keys())
    scores.extend(score.values())
    for counter in range(len(players)):
        hasMaxScore = findMaxValue(scores, players)
    if len(hasMaxScore) > 1:
        if maxScore in [7, 3, 2]:
            for hand in range(len(maxPairValue)):
                if maxPairValue[hand] != []:
                    if int(maxPairValue[hand]) > largestPair:
                        hasLargestPair.clear()
                        largestPair = int(maxPairValue[hand])
                        hasLargestPair.append(hand)
                    elif int(maxPairValue[hand]) == largestPair:
                        hasLargestPair.append(hand)
            if len(hasLargestPair) > 1:
                print("The result is a draw between the following players: ", end="")
                print(hasLargestPair)
                sys.exit()
            else:
                print("The winner is player ", end="")
                print(hasLargestPair)
        else:
            print("The result is a draw between the following players: ", end="")
            print(hasMaxScore)
    else:
        print("The winner is player ", end="")
        print(hasMaxScore)


def scoreHands(cardsList, straight, sameCardCount, hasHighestCard):
    playerScore = {}
    for hand in range(len(cardsList)):
        if straight[hand] == 1:
            isSameSuit = checkforSameSuit(cardsList[hand])  # check for straight in same suit
            if isSameSuit == 1:
                playerScore[hand] = 8  # has straight in same suit
                print("Player " + str(hand) + " has a straight flush")
                continue
            else:
                playerScore[hand] = 4  # straight but not in same suit
                print("Player " + str(hand) + " has a straight")
                continue
        sameCard = max(sameCardCount[hand].values())  # four of a kind
        if sameCard == 4:
            playerScore[hand] = 7
            print("Player " + str(hand) + " has four cards of a kind")
            continue
        if sameCard == 3 and 2 in sameCardCount[hand].values():  # three of a kind and another pair (full house)
            playerScore[hand] = 6
            print("Player " + str(hand) + " has a full house")
            continue
        if checkforSameSuit(cardsList[hand]) == 1:
            playerScore[hand] = 5  # check for flush (all cards in same suit)
            print("Player " + str(hand) + " has a flush")
            continue
        if sameCard == 3:  # three of a kind
            playerScore[hand] = 3
            print("Player " + str(hand) + " has three cards of a kind")
            continue
        if sameCard == 2:  # single pair
            playerScore[hand] = 2
            print("Player " + str(hand) + " has a pair")
            continue
        if hand in hasHighestCard:  # highest card
            playerScore[hand] = 1
            print("Player " + str(hand) + " has the highest card")
            continue
        playerScore[hand] = 0
        print("Player " + str(hand) + " sucks")
    return playerScore


generate_deck()
numofPlayers = get_num_of_players()
hands = setupHands(numofPlayers)
deal_card("players", 2, hands)
print("Your cards are: ", end="")
print(hands[0])
deal_card("middle", 1, hands)
getUserInput()
deal_card("middle", 1, hands)
getUserInput()
deal_card("middle", 1, hands)
cardsList = getCardsList(hands)
cardsList = [['S3', 'S4', 'S5', 'S6', 'S7'], ['C3', 'C4', 'C5', 'C6', 'C2'], ['C4', 'C1', 'S3', 'D6', 'D5']]
#cardsList = [['C6', 'D6', 'S3', 'D10', 'D6'], ['C6', 'D6', 'S3', 'D10', 'D6'], ['C4', 'C1', 'S3', 'D6', 'D5']]
straight = checkforStraight(cardsList)
print("Card List = ", end="")
print(cardsList)
sameCardCount, maxPairValue = checkforSameCards(cardsList)
print("Same Card Count = ", end="")
print(sameCardCount)
hasHighestCard = getHighestCard(cardsList)
score = scoreHands(cardsList, straight, sameCardCount, hasHighestCard)
print("Score = ", end="")
print(score)
determineWinner(score, maxPairValue)
