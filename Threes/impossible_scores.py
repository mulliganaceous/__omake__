from card_combinations import *
from colorama import init
import numpy as np

init(autoreset=True)
CARDNAME = ["One/Two", "Trin", "Thumbert", "Treycee", "Tristine", "Torbus", "Traven", "Threejay", "Triad", "Triferatu", "Terrence", "Whalend", "Volleo", "Triangulous", "Triangulous²"]
results = []
impossible = []

for score in range(12, 3000003,3):
    combinations, highest = possible_combinations(score)
    cardset = None
    subtype = 0
    printlimit = 3

    # Print out possile results for this particular score
    if len(combinations) == 0:
        print("\x1b[2;30;41m{0:7d} is proven impossible\x1b[1;39;49m".format(score))
        impossible.append(score)
        subtype = 3
    else:
        cardset = list(to_cards(combinations[0]))
        
        # Print high card and lower cards
        if combinations[0][0] <= 3:
            # print("{0:7d} is a trivial game with at most a {1:s} of {2:d} one-twos.".format(score, CARDNAME[combinations[0][0]], NUM_TILES - len(combinations[0])))
            printlimit = None
        elif len(combinations[0]) > 1 and combinations[0][0] == combinations[0][1] or len(combinations[0]) > 2 and combinations[0][1] == combinations[0][2] and combinations[0][1] == combinations[0][0] - 1:
            # print("{0:7d} is a 2{1:s} game of {2:d} one-twos.".format(score, CARDNAME[combinations[0][0]], NUM_TILES - len(combinations[0])))
            subtype = 2
        elif sum(cardset[1:]) >= cardset[0]:
            # print("{0:7d} is a {1:s} game of {2:d} one-twos with enough material for {3:s}.".format(score, CARDNAME[combinations[0][0]], NUM_TILES - len(combinations[0]), CARDNAME[combinations[0][0] + 1]))
            subtype = 1
        else:
            # print("{0:7d} is a {1:s} game of {2:d} one-twos.".format(score, CARDNAME[combinations[0][0]], NUM_TILES - len(combinations[0])))
            subtype = 0
        
        # # Print combinations
        # if len(combinations) > 1:
        #     print("\tThere are {0:d} such combinations.".format(len(combinations)))
        # else:
        #     print("\tThere is only one such card combination.")
    
    # Add to results
    results.append([score, len(combinations), 10*highest + subtype])

    # Print top three card combinations, if possible (trivial ones print all)
    # for combination in combinations[0:printlimit]:
    #     cardset = list(to_cards(combination))
    #     printstring = "\t{0:s}".format(str(cardset)) # Colorama goes after, otherwise may conflict
    #     if not printlimit:
    #         highest = combination[0]
    #         printstring = printstring.replace('%s' % int(3*2**highest//2), '\x1b[1;33;40m%s\x1b[1;37;40m' % int(3*2**highest//2))
    #     else:
    #         printstring = printstring.replace('%s' % int(3*2**highest//2), '\x1b[1;33;40m%s\x1b[1;37;40m' % int(3*2**highest//2))
    #     print('\x1b[1;37;40m' + printstring)
            
print(impossible[::-1])
results = np.array(results)
np.save("impossible_scores.npy", results)