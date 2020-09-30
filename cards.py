import random

cardSymbols = ['club', 'diamond', 'heart', 'spade']
cardNumbers = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
cardDeck = []
for symbol in cardSymbols:
    for number in cardNumbers:
        card = {'symbol':symbol,'number':number}
        cardDeck.append(card)
print('ไพ่ในสำรับมีทั้งหมดเป็น')
print(cardDeck)
print('********')



players = ['Mr.M', 'Mr.N', 'Miss.O', 'Miss.P']

for player in  players:
    playerDeck = []
    totalPlayerPoint = 0
    playerSymbol = []
    playerNumber = []
    cardRandom = random.choice(cardDeck)
    playerDeck.append(cardRandom)
    cardDeck.remove(cardRandom)
    cardRandom = random.choice(cardDeck)
    playerDeck.append(cardRandom)
    cardDeck.remove(cardRandom)
    print(f'{player} ได้ไพ่เป็น {playerDeck}')

    for playerCard in playerDeck:
        playerSymbol.append(playerCard['symbol'])
        playerNumber.append(playerCard['number'])
        if playerCard['number'] not in ['10','J','Q','K','A']:
            playerPoint = int(playerCard['number'])
            totalPlayerPoint += playerPoint
        else:
            playerPoint = 0
            totalPlayerPoint += playerPoint
        if totalPlayerPoint >= 10:
            totalPlayerPoint -= 10
        if totalPlayerPoint > 7:
            pokMessage = "ป็อก"
        else:
            pokMessage = ""
        if len(playerSymbol) == 2:
            if playerSymbol[0] == playerSymbol[1] or playerNumber[0] == playerNumber[1]:
                dengMessage = "2 เด้ง"
            else:
                dengMessage = ""     
        else:
            pass
            
    print(f'เป็น {pokMessage} {totalPlayerPoint} แต้ม {dengMessage}')