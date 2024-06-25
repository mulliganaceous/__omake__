import numpy as np
import matplotlib.pyplot as plt

card_combination_table = np.load("impossible_scores.npy")
impossibles = card_combination_table[card_combination_table[:,1] == 0]
rank_colors = ["blue","gray","gray","gray","#e8b280",\
               "#e9826e","#dd6044","#edda7c","#ead163", \
               "#dbbc49","#e6c541","#81d89b","#448958","black"]
subrank_types = ["o","D","+","x"]

fig, axs = plt.subplot_mosaic([['linear-log']], layout='constrained')
ax = axs['linear-log']
ax.set_yscale('linear')
plt.xlim((-60,500))

subtable = card_combination_table[card_combination_table[:,2] < 40]
ax.scatter(subtable[:,1], subtable[:,0], c=(rank_colors[1],0.25))
subtable = card_combination_table[card_combination_table[:,2] % 10 == 3]
ax.scatter(subtable[:,1] - 50, subtable[:,0], c=('red',1/25), marker='x', s=5)
for k in range(4,14):
    for j in range(0,3):
        subtable = card_combination_table[card_combination_table[:,2] == 10*k + j]
        ax.scatter(subtable[:,1], subtable[:,0], c=(rank_colors[k],1/k), marker=subrank_types[j])
        plt.ylim((0,np.max(subtable[:,0])))
        plt.savefig("Rank{0:0d}-{1:d}".format(k,j))

plt.show()
print(impossibles)