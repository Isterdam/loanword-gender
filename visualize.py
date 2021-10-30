import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.pyplot import figure
import numpy as np
from matplotlib import colors
from read_csv import *

data = np.ma.array([answer for answer in sorted_answers.values()]).transpose()

# create discrete colormap
cmap = colors.ListedColormap(['lightgrey', 'dimgrey'])
# 0/en is black, 1/ett is gray
bounds = [-0.1, 0.5, 1.1]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
fig.set_size_inches(15, 7)
ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines
ax.grid(which="minor")
ax.tick_params(which="minor", size=0)
ax.set_yticks(range(len(words)));
ax.set_yticklabels(list(ett_count.keys()), rotation='horizontal', fontsize=8)
ax.set_xticks(range(len(sorted_answers)));
ax.set_xticklabels(list(sorted_answers.keys()), rotation='vertical', fontsize=6)
ax.set_xlabel('respondent')
ax.set_ylabel('borrowing')

lightgrey_patch = mpatches.Patch(color='lightgrey', label='en')
dimgrey_patch = mpatches.Patch(color='dimgrey', label='ett')
plt.legend(handles=[lightgrey_patch, dimgrey_patch], loc="lower right")

plt.show()
