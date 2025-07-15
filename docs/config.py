import warnings
warnings.filterwarnings('ignore')

import numpy as np
np.random.seed(0)

import pandas as pd
pd.options.display.max_columns = 999
pd.options.display.max_rows = 999

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['legend.fontsize'] = 28
plt.rcParams['lines.markersize'] = 18
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#666666', '#E69F00', '#56B4E9', '#009E73',
                                                    '#F0E442', '#0072B2', '#D55E00', '#CC79A7'])
plt.rcParams['font.family'] = 'Helvetica Neue' 
plt.rcParams['font.size'] = 32

from myst_nb import glue
