
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.patches import Rectangle
from pylab import *
import matplotlib.ticker as ticker
import sys
sys.path.append("..")

plt.rc('font', family='Times New Roman')
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["axes.titleweight"] = "bold"
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

name_list = [r"ALLD", r"ALLC", r"HardMajority", r"TFT", r"GTFT", r"WSLS", r"CIC", r"CURE2", r"Extort2_independent", r"Generous_independent"]
titles = ["(a) MCSUC-ALLD", "(b) MCSUC-ALLC", "(c) MCSUC-HardMajority", "(d) MCSUC-TFT", "(e) MCSUC-GTFT", "(f) MCSUC-WSLS", "(g) MCSUC-CIC", "(h) MCSUC-CURE", "(i) MCSUC-Extort2", "(j) MCSUC-Generous2"]

tau_list = [1, 1, 1, 5]
action_num_list = [2, 2, 2, 3]
save_path = r''
sim_line_width = 8
num_line_width = 2

x_values = np.arange(-1, 4.05, 0.05)
fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(25, 10))
for i, name in enumerate(name_list):
    MCSUC_data = pd.read_csv(save_path + r"evolution_result_MCSUC_vs_" + name + ".csv", delimiter=',')
    MCSUC_data = MCSUC_data.iloc[:, 2]
    current_data = 1 - MCSUC_data

    ax = axes[i // 5, i % 5]

    if 'CURE2' in name:
        label_name = 'CURE'
    elif 'Generous_independent' in name:
        label_name = 'Generous2'
    else:
        label_name = name.split('_')[0]

    sns.lineplot(x=x_values, y=MCSUC_data, ax=ax, label=r'MCSUC',color='b',linewidth=num_line_width)
    sns.lineplot(x=x_values, y=current_data, ax=ax, label=label_name,color='salmon',linewidth=num_line_width)

    ax.legend(fontsize=18)


    gamma = 0.1
    ax.set_facecolor('none')

    background_color = np.array(
        [[43 / 255, 85 / 255, 125 / 255, gamma], [69 / 255, 189 / 255, 155 / 255, gamma],
         [240 / 255, 81 / 255, 121 / 255, gamma],
         [253 / 255, 207 / 255, 110 / 255, gamma]])
    ax.add_patch(Rectangle((-1, -0.02), 1, 1.04, facecolor=background_color[0]))
    ax.text(-0.75, 0.15, "SH", fontsize=18)
    ax.add_patch(Rectangle((0, -0.02), 1, 1.04, facecolor=background_color[1]))
    ax.text(0.25, 0.15, "PD", fontsize=18)
    ax.add_patch(Rectangle((1, -0.02), 2, 1.04, facecolor=background_color[2]))
    ax.text(1.16, 0.15, "SD", fontsize=18)


    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=1))
    ax.grid(False)
    ax.spines['bottom'].set_linewidth('1.5')
    ax.spines['left'].set_linewidth('1.5')
    tick_params(which='major', width=1)
    if i>=5:
        ax.set_xlabel("b", fontsize=20)
    ax.set_ylabel(None)
    ax.set_title(' ')
    ax.tick_params(labelsize=20)

    ax.set_xlim([-1, 1.4])
    ax.set_ylim([-0.02, 1.02])
    ax.set_title(titles[i], fontsize=23)
    if i == 0 or i == 5:
        ax.set_ylabel("Proportion", fontsize=20)

plt.savefig('robust.pdf', format="pdf", bbox_inches='tight', dpi=900)

