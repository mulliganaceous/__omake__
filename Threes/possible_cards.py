NUM_TILES = 4*4
NUM_LOCK = 8
MAX_RANK = 13

def _cards(cards: list[int]):
    return map(lambda x : 3*2**(x - 1), cards)

def _value(cards: list[int]):
    return map(lambda x : 3**x, cards)

def _cardsmult(cards: list[int], mults: list[int]):
    return map(lambda x, m: (3*2**(x - 1), m), cards, mults)

def possible_combinations(score: int, debug=True) -> list[int]:
    '''
    Iterative stack method of obtaining the possible combinations of cards in a game of Threes.
    '''
    if score < 3:
        raise Exception("Score is not possible")
    answer = []
    cards = []
    mults  = []
    rem = score
    rank = MAX_RANK
    mult = 1
    while score < 3**rank:
        rank -= 1
    print("Maximum rank: {0:d}".format(3*2**(rank - 1)))
    while NUM_LOCK*3**rank > score:
        cards.append(rank)
        mults.append(mult)
        rem -= 3**rank
        while len(cards):
            if debug:
                print("[{0:2d}]\t{1:d}\t{2:s}".format(len(cards),sum(_value(cards)),str(list(_cards(cards)))))
            if rem == 0:
                answer.append(1*cards) # clone cards
            while rank > 0 and 3**rank > rem:
                rank -= 1
                mult = 0
            if rank == 0 or len(cards) == NUM_TILES or mult == NUM_LOCK or NUM_LOCK*3**rank < rem:
                rank = cards.pop()
                mults.pop()
                rem += 3**rank
                rank -= 1
                mult = 0
            else:
                mult += 1
                cards.append(rank)
                mults.append(mult)
                rem -= 3**rank
    return answer

if __name__ == "__main__":
    import numpy as np
    import sys
    from colorama import init
    init(autoreset=True)
    np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)
    while True:
        try:
            score = int(input("Enter a score: "))
            answer = possible_combinations(score)
            answer = map(lambda x : list(_cards(x)) + [0]*(NUM_TILES - len(x)), answer)
            answer = np.array(list(answer))
            highest = None
            if len(answer) > 0:
                highest = answer[0][0]
            print("\x1b[1;33;40m{0:s}".format(str(answer)).replace(' 0', '\x1b[1;36;40m -\x1b[1;33;40m').replace('%s' % highest, '\x1b[1;31;40m%s\x1b[1;33;40m' % highest))
        except ValueError:
            pass
