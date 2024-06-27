import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

card_combination_table = np.load("impossible_scores.npy")
impossibles = card_combination_table[card_combination_table[:,1] == 0]
rank_colors = ["blue","gray","gray","gray","#e8b280",\
               "#e9826e","#dd6044","#edda7c","#ead163", \
               "#dbbc49","#e6c541","#81d89b","#448958","black"]
subrank_types = [["o",10],["D",5],["+",21],["x",10]]

def possible_combinations():
    fig, axs = plt.subplot_mosaic([['possible_combinations']], layout='constrained')
    ax = axs['possible_combinations']
    ax.set_yscale('linear')

    subtable = card_combination_table[card_combination_table[:,2] < 40]
    ax.scatter(subtable[:,1], subtable[:,0], c=(rank_colors[1],0.25), s = subrank_types[0][1])
    plt.xlim((-5,np.max(subtable[:,1])))
    plt.savefig("Rank{0:0d}-{1:d}".format(0,0))
    print("Rank{0:0d}-{1:d}".format(0,0))

    subtable = card_combination_table[card_combination_table[:,2] % 10 == 3]
    ax.scatter(subtable[:,1], subtable[:,0], c=('red',1/50), marker='x', s=5)
    for k in range(4,14):
        for j in range(0,3):
            subtable = card_combination_table[card_combination_table[:,2] == 10*k + j]
            ax.scatter(subtable[:,1], subtable[:,0], c=(rank_colors[k],12/k**2.5), marker=subrank_types[j][0], s=subrank_types[j][1])
            if len(subtable) > 0:
                plt.ylim((0,np.max(subtable[:,0])))
                plt.savefig("Rank{0:0d}-{1:d}".format(k,j))
                print("Rank{0:0d}-{1:d}".format(k,j))
    k = 13
    for j in range(6, 12):
        subtable = card_combination_table[card_combination_table[:,2] == 10*k + j]
        ax.scatter(subtable[:,1], subtable[:,0], c=(rank_colors[k],12/k**3), marker=subrank_types[2][0], s=subrank_types[2][1])
        if len(subtable) > 0:
            plt.ylim((np.min(subtable[:,0]),np.max(subtable[:,0])))
        plt.savefig("Rank{0:0d}-{1:d}".format(k,j))
        print("Rank{0:0d}-{1:d}".format(k,j))

    plt.show()

def one_two_combinations():
    fig, axs = plt.subplot_mosaic([['possible_combinations']], layout='constrained')
    ax = axs['possible_combinations']
    ax.set_yscale('linear')
    plt.figure(figsize=(9,16))

    subtable = card_combination_table[card_combination_table[:,2] < 40]
    ax.scatter(subtable[:,1], subtable[:,3], c=(rank_colors[1],0.25), s = subrank_types[0][1])
    plt.savefig("OneTwo{0:0d}-{1:d}".format(0,0))
    
    for k in range(4,14):
        for j in range(0,3):
            fig.clear()
            fig, axs = plt.subplot_mosaic([['possible_combinations']], layout='constrained')
            ax = axs['possible_combinations']
            subtable = card_combination_table[card_combination_table[:,2] == 10*k + j]
            ax.scatter(subtable[:,1], subtable[:,3], c=(rank_colors[k],12/k**2.5), marker=subrank_types[j][0], s=subrank_types[j][1])
            if len(subtable) > 0:
                plt.savefig("OneTwo{0:0d}-{1:d}".format(k,j))
                print("OneTwo{0:0d}-{1:d}".format(k,j))
    k = 13
    for j in range(6, 12):
        fig.clear()
        fig, axs = plt.subplot_mosaic([['possible_combinations']], layout='constrained')
        ax = axs['possible_combinations']
        subtable = card_combination_table[card_combination_table[:,2] == 10*k + j]
        ax.scatter(subtable[:,1], subtable[:,3], c=(rank_colors[k],12/k**3), marker=subrank_types[2][0], s=subrank_types[2][1])
        plt.savefig("OneTwo{0:0d}-{1:d}".format(k,j))
        print("OneTwo{0:0d}-{1:d}".format(k,j))

    plt.show()

def impossible_percentage_rank(BASE, SUBINTERVAL):

    subtable = card_combination_table[card_combination_table[:,2] < 40]
    fig, axs = plt.subplot_mosaic([['percentage_impossible']], layout='constrained', figsize=(64,36))
    ax = axs['percentage_impossible']
    ax.set_yscale('linear')

    subtable = card_combination_table[card_combination_table[:,2] % 10 == 3]
    ax.scatter(subtable[:,1] - 16, np.log(subtable[:,0])/np.log(BASE), c=('red',1/50), marker='x', s=5)

    subtable = card_combination_table[card_combination_table[:,2] < 40]
    ax.scatter(subtable[:,1], np.log(subtable[:,0])/np.log(BASE), c=(rank_colors[1],0.64), s = subrank_types[0][1])
    plt.xlim((-5,500))
    plt.savefig("Rank{0:0d}-{1:d}".format(0,0))
    print("Rank{0:0d}-{1:d}".format(0,0))

    for k in range(4,14):
        for j in range(0,3):
            subtable = card_combination_table[card_combination_table[:,2] == 10*k + j]
            ax.scatter(subtable[:,1], np.log(subtable[:,0])/np.log(BASE), c=(rank_colors[k],12/k**2.5), marker=subrank_types[j][0], s=subrank_types[j][1])
            if len(subtable) > 0:
                plt.savefig("Rank{0:0d}-{1:d}".format(k,j))
                print("Rank{0:0d}-{1:d}".format(k,j))
    k = 13
    for j in range(6, 12):
        subtable = card_combination_table[card_combination_table[:,2] == 10*k + j]
        ax.scatter(subtable[:,1], np.log(subtable[:,0])/np.log(BASE), c=(rank_colors[k],12/k**3), marker=subrank_types[2][0], s=subrank_types[2][1])
        # plt.savefig("Rank{0:0d}-{1:d}".format(k,j))
        print("Rank{0:0d}-{1:d}".format(k,j))

    ranks = []
    for k in range(9*SUBINTERVAL,int((12 + np.log(4)/np.log(BASE) + 5)*SUBINTERVAL)):
        # print(10**((k - 1)/10), 10**(k/10), 10**((k + 1)/10))
        subtable = card_combination_table[ card_combination_table[:,0] >= BASE**(k/SUBINTERVAL) ]
        subtable = subtable[ subtable[:,0] < BASE**((k + 1)/SUBINTERVAL) ]
        impossible = subtable[ subtable[:,2] % 10 == 3 ]
        if len(subtable) > 0:
            impossibility = len(impossible)/len(subtable)
            print("{0:8d}\t[ {1:6.2f}% ] {3:d}/{2:d} impossible".format(int(np.ceil(BASE**(k/SUBINTERVAL))), impossibility*100, len(subtable), len(impossible)))
            ranks.append([k/SUBINTERVAL, impossibility])
        else:
            print("{0:8d}\t is empty".format(int(np.ceil(BASE**(k/SUBINTERVAL)))))
            
    ranks = np.array(ranks)
    ax.plot(500*ranks[:,1],ranks[:,0], 'r')
    ax.yaxis.set_major_formatter(lambda y, pos : "{0:d}".format(int(3**y)))
    ax.yaxis.set_minor_formatter(lambda y, pos : "{0:d}".format(int(3**y)))
    ax.xaxis.set_minor_formatter(ticker.FormatStrFormatter("%d%%"))

    secax = ax.secondary_xaxis('top', functions=(lambda x: x / 5, lambda x : x * 5))
    ax.set_xlabel('number of combinations (exact)')
    ax.set_ylabel('score')
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1,0))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(1,np.log(4)/np.log(3)))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(1,np.log((3**13+1)/2)/np.log(3) - 12))
    ax.set_title('Number of card combinations and impossible scores in Threes')
    secax.set_xlabel('percentage impossible (in increment)')

    plt.savefig("Impossible_Percentage", dpi=120)

    for j in range(6, 12):
        subtable = card_combination_table[card_combination_table[:,2] == 10*k + j]
        if len(subtable) > 0:
            plt.ylim((np.min(np.log(subtable[:,0])/np.log(BASE)),np.max(np.log(subtable[:,0])/np.log(BASE))))
            plt.savefig("Impossible_Percentage 13-{0:d}".format(j), dpi=120)
    
    # plt.show()

impossible_percentage_rank(3,16)
