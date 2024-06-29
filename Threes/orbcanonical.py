import numpy as np
import matplotlib.pyplot as plt

import omgpy

MAXLIMIT = 12000
orbdrops = omgpy.Best_Combination([1, 3, 7, 17, 37, 73, 149, 307, 617, 1237, 2477])
orbdrops.all_combinations(MAXLIMIT)

fig, axs = plt.subplot_mosaic([['orbdrop-greedy']], layout='constrained', figsize=(16,9))
ax = axs['orbdrop-greedy']
ax.set_yscale('linear')
plt.xlim((0,MAXLIMIT + 1))

z = []
y = []
xf = []
yf = []
xff = []
yff = []
for k in range(MAXLIMIT + 1):
    stack, best = orbdrops.all_combinations(k)
    z.append((stack, best))
    if len(best) >= 2:
        y.append(best[1])
        if len(best) > 2:
            for j in range(2,len(best)-1):
                xff.append(k)
                yff.append(best[j])
            xf.append(k)
            yf.append(best[-1])

    else:
        y.append(0)

ax.scatter(np.linspace(0,MAXLIMIT, MAXLIMIT + 1), y)
ax.scatter(xf, yf, c='r')
ax.scatter(xff, yff, c='y')
ax.set_xlabel('experience')
ax.set_ylabel('orbs dropped')
ax.set_title('coin change problem for Minecraft orbs')

plt.savefig("orb_change_%5d" % MAXLIMIT, dpi=120)
plt.show()