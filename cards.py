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
    cardRandom = random.choice(cardDeck)
    playerDeck.append(cardRandom)
    cardDeck.remove(cardRandom)
    cardRandom = random.choice(cardDeck)
    playerDeck.append(cardRandom)
    cardDeck.remove(cardRandom)
    print(f'{player} ได้ไพ่เป็น {playerDeck}')