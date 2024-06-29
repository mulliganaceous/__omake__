NUM_TILES = 4*4
NUM_LOCK = 8
MAX_RANK = 13
MIN_TILES = 4

def to_cards(cards: list[int], mults: list[int] = None):
    if not mults:
        return map(lambda x : 3*2**(x - 1), cards)
    return map(lambda x, m: (3*2**(x - 1), m), cards, mults)

def to_value(cards: list[int]):
    return map(lambda x : 3**x, cards)

def possible_combinations(score: int, debug=False) -> tuple[list[int], int]:
    '''
    Iterative stack method of obtaining the possible combinations of cards in a game of Threes.
    '''
    if score < 3:
        raise Exception("Score is too low")
    
    answer = []
    cards = []
    mults  = []
    rem = score
    rank = MAX_RANK
    mult = 1
    
    while score < 3**rank:
        rank -= 1
    
    highest = rank
    while 4*NUM_LOCK*3**(rank - 1) >= score: # From double lock
        mult = 1
        cards.append(rank)
        mults.append(mult)
        rem -= 3**rank
        while len(cards):
            if debug:
                print("[{0:2d}]\t{1:d}\t{2:s}".format(len(cards),sum(to_value(cards)),str(list(to_cards(cards, mults))),rem).replace(" ",""))

            if rem == 0 and len(cards) >= MIN_TILES:
                answer.append(1*cards) # clone cards
            while rank > 0 and 3**rank > rem:
                rank -= 1
                mult = 0
                
            if rank == 0 or len(cards) == NUM_TILES or rank == 1 and mult == NUM_LOCK or 4*NUM_LOCK*3**(rank - 1) < rem:
                # Finish recursive call
                rank = cards.pop()
                mults.pop()
                rem += 3**rank
                rank -= 1
                mult = 0
            elif mult == NUM_LOCK:
                # Move on to next card
                rank -= 1
                mult = 1
                cards.append(rank)
                mults.append(mult)
                rem -= 3**rank
            else:
                # Add next copy
                mult += 1
                cards.append(rank)
                mults.append(mult)
                rem -= 3**rank
    return answer, highest

if __name__ == "__main__":
    import numpy as np
    import sys
    from colorama import init
    init(autoreset=True)
    np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)
    while True:
        try:
            score = input("Enter a score: ")
            if score == "exit()":
                exit(0)
            score = int(score)
            answer = possible_combinations(score, True)
            highest = 3*2**(answer[1] - 1)
            answer = answer[0]
            answer = map(lambda x : list(to_cards(x)) + [0]*(NUM_TILES - len(x)), answer)
            answer = np.array(list(answer))
            str1 = "{0:s}".format(str(answer))
            str1 = str1.replace('%s' % highest, '\x1b[1;31;40m%s\x1b[1;33;40m' % highest).replace(' 0', '\x1b[1;36;40m -\x1b[1;33;40m')
            str2 = "There are {0:d} possible card combinations for scoring exactly {1:d}. It corresponds to the {2:d} card.\n".format(len(answer),score,highest)
            print("\x1b[1;33;40m" + str1)
            print(str2)
        except ValueError:
            pass
        except Exception:
            print("Score is too low.")
