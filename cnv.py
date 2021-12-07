#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:21:05 2021

@author: roma
"""

from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.decomposition import PCA
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
file='/home/roma/cnv/df_matrix.csv'
df=pd.read_csv(file, sep=',', index_col=0)
sns.clustermap(df)
df_matrix_normalized=(df - df.mean()) / df.std()
Z = linkage(df, 'ward')
k = dendrogram(Z, labels=df.index, leaf_rotation=90)
plt.savefig('./testik.png', dpi=300)

pca = PCA(n_components=2)
pheno = pd.read_csv('/home/roma/cnv/samples_out_backup.txt', sep='\t')

pheno_list = []
for i, row in df.iterrows():
    pheno_list.append(str(pheno[pheno['sample.id'].str.contains(i)]['BT']).split(' ')[4].split('\n')[0])
    
df['Pheno'] = pheno_list


features = list(df.columns)
del features[-1]
x = df.loc[:, features].values
y = df.loc[:,['Pheno']].values
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, df[['Pheno']].reset_index(drop=True)], axis = 1)


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 


ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['1', '2']
colors = ['r', 'g' ]
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['Pheno'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)