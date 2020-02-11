import random
suits = {"H":"Hearts", "C":"Clubs", "D":"Diamonds", "S":"Spades"}
faces = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]


def generateDeck(suits,faces):
    deck = []
    for suit in suits.keys():
        for face in faces:
            deck.append(suit + face)
    return deck


def getNumofPlayers():
    playerNum = 0
    while playerNum < 3:
        try:
            playerNum = int(input("Please enter the number of players: "))
            if playerNum < 3:
                print("There must be a minimum of three players. Please try again.")
        except ValueError:
            print("Invalid number. Please try again.")
    return playerNum


def setupHands(playerNum):
    hands = []
    for playerHand in range(playerNum):
        hands.append([])
    return hands


def nextP(lastPlayer):
    if lastPlayer < playerNum -1 and len(deck) != 52:
        nextPlayer = lastPlayer + 1
    else:
        nextPlayer = 0
    return nextPlayer


def dealCards(deck,hands,nextPlayer=0):
    while len(deck) > 0:
        dealtCard = deck.pop()
        if dealtCard == "S7":
            startingPlayer = nextPlayer
        hands[nextPlayer].append(dealtCard)
        lastPlayer = nextPlayer
        nextPlayer = nextP(lastPlayer)
    return hands,startingPlayer


def findValidCards(playedCard="",validCards=[]):
    sevens = ["H7", "D7", "C7"]
    if playedCard == "NA": #no card was played
        print("The valid cards are ", end="")
        print(validCards)
        return validCards
    elif playedCard == "":
        validCards.append("S7")
    else:
        playedCard = convNametoNum(playedCard)
        suit = playedCard[0]
        face = playedCard[1:]
        nextCard = suit + str(int(face)+1)
        prevCard = suit + str(int(face)-1)
        if nextCard not in validCards and 7 <= int(face) < 13:
            validCards.append(convNumtoName(nextCard))
        if prevCard not in validCards and 7 >= int(face) > 1:
            validCards.append(convNumtoName(prevCard))
    if playedCard == "S7":
        validCards.extend(["H7","C7","D7"])
    validCards.sort()
    print("The valid cards are ", end="")
    print(validCards)
    return validCards


def convNametoNum(card):
    convert = {"A":1,"J":11,"Q":12,"K":13}
    face = card[1:]
    suit = card[0]
    if face in convert.keys():
        face = convert[face]
    card = suit + str(face)
    return card


def convNumtoName(card):
    convert = {"1":"A","11":"J","12":"Q","13":"K"}
    face = card[1:]
    suit = card[0]
    if face in convert.keys():
        face = convert[face]
    card = suit + str(face)
    return card


def convertNumtoTxt(card):
    faceConv = {"A":"Ace","J":"Jack","Q":"Queen","K":"King"}
    suitConv = {"H":"Hearts","D":"Diamonds","S":"Spades","C":"Clubs"}
    suit = card[0:1]
    face = card[1:]
    if face in faceConv.keys():
        face = faceConv[face]
    suit = suitConv[suit]
    return suit, face


def playCard(hands,validCards,nextPlayer,cardsList):
    sevens = {"H7","D7","C7"}
    hasSeven = []
    print("Current player's hand = ",end="")
    print(hands[nextPlayer])
    for counter in range(len(validCards)):
        if validCards[counter] in hands[nextPlayer]:
            if validCards[counter] in sevens:
                hasSeven.append(validCards[counter])
            if validCards[counter] not in sevens:
                playedCard = validCards[counter]
                #print("Played Card = " + playedCard)
                suit,face = convertNumtoTxt(playedCard)
                print("Player " + str(nextPlayer) + " played the " + str(face) + " of " + suit)
                hands[nextPlayer].remove(playedCard)
                cardsList.append(validCards[counter])
                validCards.remove(validCards[counter])
                lastPlayer = nextPlayer
                return lastPlayer,playedCard,cardsList
    if hasSeven != []:
        playedCard = hasSeven.pop()
        suit, face = convertNumtoTxt(playedCard)
        print(str(nextPlayer) + " played the " + str(face) + " of " + suit)
        hands[nextPlayer].remove(playedCard)
        cardsList.append(playedCard)
        validCards.remove(playedCard)
        lastPlayer = nextPlayer
        return lastPlayer,playedCard,cardsList
    playedCard = "NA"
    lastPlayer = nextPlayer
    return lastPlayer,playedCard,cardsList


def promptUser(lastPlayer):
    cardPlayed = 0
    hasValidCard = 0
    hands[nextPlayer].sort()
    print("Your hand: ",end="")
    print(hands[nextPlayer])
    for counter in range(len(hands[nextPlayer])):
        if hands[nextPlayer][counter] in validCards:
            hasValidCard = 1
    while cardPlayed != 1:
        try:
            userCard = input("Please select a card to play or press enter to pass: ")
        except TypeError:
            print("Invalid input. Please try again.")
        if userCard == "" and hasValidCard == 0:
            userCard = "NA"
            print("Pass.")
            lastPlayer = nextPlayer
            return lastPlayer,userCard,cardsList
        elif userCard == "" and hasValidCard == 1:
            print("You have a valid card and must play it.")
        elif userCard != "":
            userCard = userCard.upper()
            if userCard not in validCards or userCard not in hands[nextPlayer]:
                print("The card you selected was invalid. Please try again.")
            else:
                cardPlayed = 1
    suit, face = convertNumtoTxt(userCard)
    print("You played the " + str(face) + " of " + suit)
    hands[nextPlayer].remove(userCard)
    cardsList.append(userCard)
    validCards.remove(userCard)
    lastPlayer = nextPlayer
    return lastPlayer, userCard, cardsList


def checkForWinner(lastPlayer, hands):
    if hands[lastPlayer] == []:
        global winner
        winner = 1
    return winner


deck = generateDeck(suits, faces)
random.shuffle(deck)
playerNum = getNumofPlayers()
hands = setupHands(playerNum)
hands, startingPlayer = dealCards(deck, hands)
nextPlayer = startingPlayer
print("Player " + str(startingPlayer) + " has the 7 of Spades and will start the game.")
cardsList = []
winner = 0
playedCard = "";

while winner == 0:
    validCards = findValidCards(playedCard)
    cardsList.sort()
    if nextPlayer != 0:
        lastPlayer,playedCard,cardsList = playCard(hands,validCards,nextPlayer,cardsList)
    else:
        lastPlayer,playedCard,cardsList = promptUser(nextPlayer)
    checkForWinner(lastPlayer,hands)
    nextPlayer = nextP(lastPlayer)
    if nextPlayer == 0 and winner != 1:
        print("You are the next player")
    elif nextPlayer != 0 and winner != 1:
        print("The next player is " + str(nextPlayer))

if lastPlayer == 0:
    print("You have won the game!")
else:
    print("Player " + str(lastPlayer) + " has won the game")
