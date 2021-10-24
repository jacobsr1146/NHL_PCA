import pandas as pd
import numpy as np
import random
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
from scrubData import importfile

playerinfo, playerstats = importfile("skaters_2020-21.csv", "goalies_2020-21.csv")
#playerstats.drop(columns=['icetime', 'timeOnBench', 'shifts', 'I_F_shifts', 'games_played', 'iceTimeRank'], axis=1, inplace = True)

pca = PCA()
pca.fit(playerstats)
pca_data = pca.transform(playerstats)

## PC Graph
# per_var = np.round(pca.explained_variance_ratio_*100, decimals=1)
# labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
# plt.bar(x=range(1, len(per_var)+1), height=per_var, tick_label=labels)
# plt.ylabel('Percentage of Explained Variance')
# plt.xlabel('Principal Component')
# plt.title('Scree Plot')
# #plt.show()

## Plotting data with PC vs. PC2
# pca_df = pd.DataFrame(pca_data, index=[list(playerinfo['name'].to_numpy())], columns=labels)
# plt.scatter(pca_df.PC1, pca_df.PC2)
# plt.title('My PCA Graph')
# plt.xlabel('PC1 - {0}%'.format(per_var[0]))
# plt.ylabel('PC2 - {0}%'.format(per_var[1]))
# plt.show()


# Determine which variables had the biggest influence on PC1
variables = list(playerstats.columns.values)
loading_scores = pd.Series(pca.components_[0], index=variables)
sorted_loading_scores = loading_scores.reindex(loading_scores.abs().sort_values(ascending=False).index)
top_10_variables = sorted_loading_scores[0:10].index.values

print("top 10 variables:", top_10_variables)

for i in range(10):
    print(top_10_variables[i],": ", sorted_loading_scores[i])

