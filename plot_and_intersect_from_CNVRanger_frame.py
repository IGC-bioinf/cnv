import pandas as pd
import sys
file = '/home/roma/cnv/proj_cnv/done/regions_without_test_abr.csv' ############################# INPUTFILE
df = pd.read_csv(file)
df = df.sort_values(by='MinPvalue')

import numpy as np
import seaborn as sns
#from scipy.stats import uniform, randint


df['-logp'] = -np.log10(df.MinPvalue); df = df.sort_values(['seqnames','start'])
df.reset_index(inplace=True, drop=True); df['i'] = df.index

# Generate Manhattan plot: (#optional tweaks for relplot: linewidth=0, s=9)
plot = sns.relplot(data=df, x='i', y='-logp', aspect=3.7, 
                   hue='seqnames', palette = 'bright', legend=None) 
chrom_df=df.groupby('seqnames')['i'].median()
plot.ax.set_xlabel('Chromosome'); plot.ax.set_xticks(chrom_df);
plot.ax.set_xticklabels(chrom_df.index)
plot.fig.suptitle('Manhattan plot')
plot.savefig(sys.argv[2]) ###################
print('PLOT DONE')

cnv = '/home/roma/cnv/proj_cnv/big_cnv_with_genes_uniq.txt'
cnv_df = pd.read_csv(cnv, sep='\t', header=None)
cnv_df[0] = cnv_df[0].str.replace('chr', '', regex=False)
cnv_df[0] = cnv_df[0].str.replace('X', '25', regex=False)
cnv_df[0] = cnv_df[0].str.replace('Y', '27', regex=False)
cnv_df[0] = pd.to_numeric(cnv_df[0])
cnv_df[2] = pd.to_numeric(cnv_df[2])
cnv_df[1] = pd.to_numeric(cnv_df[1])
clean_df = pd.read_csv(file)
clean_df = df.sort_values(by='MinPvalue')
clean_df = clean_df.loc[clean_df['MinPvalue'] < 0.05].reset_index()
clean_df = clean_df.loc[clean_df['width'] > 30 ].reset_index()
clean_df = clean_df.drop(columns=['index', 'level_0'])

clean_df['seqnames'] = pd.to_numeric(clean_df['seqnames'])
clean_df['start'] = pd.to_numeric(clean_df['start'])
clean_df['end'] =  pd.to_numeric(clean_df['end'])

new_dfs = []
r=0
for chr_name, chr_df in clean_df.groupby('seqnames'):
    chr_df2 = cnv_df.loc[cnv_df[0] == chr_name]
    for i in chr_df.index:
        for k in chr_df2.index:
            if  (((chr_df2[2][k] >= chr_df['start'][i] >= chr_df2[1][k]) and (chr_df2[1][k] <= chr_df['end'][i] <= chr_df2[2][k])) or #both inside
            ((chr_df2[2][k] >= chr_df['start'][i] >= chr_df2[1][k]) and (chr_df['end'][i] >= chr_df2[2][k])) or #start inside
            ((chr_df['start'][i] <= chr_df2[1][k]) and (chr_df2[1][k] <= chr_df['end'][i] <= chr_df2[2][k])) or #end inside
            ((chr_df['start'][i] <= chr_df2[1][k]) and (chr_df['end'][i] >= chr_df2[2][k]))): #both outside
                temp_df=pd.DataFrame(columns=['chr', 'start', 'end', 'gene', 'cnv', 'Pvalue', 'Perc_of_patients', 'Perc_of_controls'])
                temp_df.loc[r, ['chr']]=[chr_df['seqnames'][i]]
                temp_df.loc[r,['start']] = [chr_df['start'][i]]
                temp_df.loc[r,['end']] = [chr_df['end'][i]]
                #temp_df.loc[r,['gene']] = [chr_df2[4][k]]
                temp_df.loc[r, ['cnv']] = [chr_df2[3][k]]
                temp_df.loc[r, ['Pvalue']] = [chr_df['MinPvalue'][i]]
                new_dfs.append(temp_df) 
                r=r+1

new_dfs = pd.concat(new_dfs)
new_dfs = new_dfs.drop_duplicates(subset = ["start"]).reset_index()
print("First DF done")
for i in range(len(new_dfs)):
    if new_dfs['cnv'][i] > 2:
        new_dfs['cnv'][i] = 'DUP'
    elif new_dfs['cnv'][i] < 2:
        new_dfs['cnv'][i] = 'DEL'
    else:
         new_dfs['cnv'][i] = 'DIP'
new_dfs = new_dfs.drop(columns=['index'])


pheno = sys.argv[3] ############################# PHENO FILE
cnv_pac = '/home/roma/cnv/proj_cnv/big_cnv.txt'
pheno_df = pd.read_csv(pheno, sep='\t')
cnv_pac_df = pd.read_csv(cnv_pac, sep='\t')




for chr_name, chr_df in new_dfs.groupby('chr'):
     chr_df2 = cnv_pac_df.loc[cnv_pac_df['chr'] == chr_name]
     for i in chr_df.index:
        pac_num=[]
        c_number = []
        for k in chr_df2.index:
             if  (((chr_df2['end'][k] >= chr_df['start'][i] >= chr_df2['start'][k]) and (chr_df2['start'][k] <= chr_df['end'][i] <= chr_df2['end'][k])) or
            ((chr_df2['end'][k] >= chr_df['start'][i] >= chr_df2['start'][k]) and (chr_df['end'][i] >= chr_df2['end'][k])) or
            ((chr_df['start'][i] <= chr_df2['start'][k]) and (chr_df2['start'][k] <= chr_df['end'][i] <= chr_df2['end'][k])) or
            ((chr_df['start'][i] <= chr_df2['start'][k]) and (chr_df['end'][i] >= chr_df2['end'][k]))):
                if chr_df['cnv'][i] == 'DUP' and chr_df2['state'][k] > 2:
                    if int(pheno_df.loc[pheno_df['sample.id'] == chr_df2['sample.id'][k]][sys.argv[6]]) == 2:
                          pac_num.append(str(pheno_df.loc[pheno_df['sample.id'] == chr_df2['sample.id'][k]]['sample.id'].reset_index()['sample.id'][0]))
                    else:
                        c_number.append(str(pheno_df.loc[pheno_df['sample.id'] == chr_df2['sample.id'][k]]['sample.id'].reset_index()['sample.id'][0]))
                elif chr_df['cnv'][i] == 'DEL' and chr_df2['state'][k] < 2:
                    if int(pheno_df.loc[pheno_df['sample.id'] == chr_df2['sample.id'][k]][sys.argv[6]]) == 2:
                          pac_num.append(str(pheno_df.loc[pheno_df['sample.id'] == chr_df2['sample.id'][k]]['sample.id'].reset_index()['sample.id'][0]))
                    else:
                        c_number.append(str(pheno_df.loc[pheno_df['sample.id'] == chr_df2['sample.id'][k]]['sample.id'].reset_index()['sample.id'][0]))
               
                        
        new_dfs.loc[i, ['Perc_of_patients']]=len(list(set(list(pac_num)))) / len(pheno_df.loc[pheno_df[sys.argv[6]]==2])
        new_dfs.loc[i, ['Perc_of_controls']]=len(list(set(list(c_number)))) / len(pheno_df.loc[pheno_df[sys.argv[6]]==1])
print ("SECOND DF DONE")
    
new_dfs1 = []

bed_file=sys.argv[4]######################### PANEL FILE
bed_df = pd.read_csv(bed_file, sep = '\t', header=None)
bed_df[0] = bed_df[0].str.replace('X', '25', regex=False)
bed_df[0] = bed_df[0].str.replace('Y', '27', regex=False)
bed_df[0]=pd.to_numeric(bed_df[0])
bed_df[1]=pd.to_numeric(bed_df[1])
bed_df[2]=pd.to_numeric(bed_df[2])

for chr_name, chr_df in new_dfs.groupby('chr'):
    chr_df2 = bed_df.loc[bed_df[0] == chr_name]
    overlapping = (chr_df['start'].apply(lambda x: chr_df2[2] >= x) & chr_df['end'].apply(lambda x: chr_df2[1] <= x)).any(axis=1)
    new_dfs1.append(chr_df.loc[overlapping, :])

new_dfs1 = pd.concat(new_dfs1)
#new_dfs1.to_csv('/home/roma/cnv/proj_cnv/regions_proc_nek.csv', index=False)


new_dfs2 = []
r=0
for chr_name, chr_df in new_dfs1.groupby('chr'):
    chr_df2 = bed_df.loc[bed_df[0] == chr_name]
    for i in chr_df.index:
        for k in chr_df2.index:
            if  (((chr_df2[2][k] >= chr_df['start'][i] >= chr_df2[1][k]) and (chr_df2[1][k] <= chr_df['end'][i] <= chr_df2[2][k])) or #both inside
            ((chr_df2[2][k] >= chr_df['start'][i] >= chr_df2[1][k]) and (chr_df['end'][i] >= chr_df2[2][k])) or #start inside
            ((chr_df['start'][i] <= chr_df2[1][k]) and (chr_df2[1][k] <= chr_df['end'][i] <= chr_df2[2][k])) or #end inside
            ((chr_df['start'][i] <= chr_df2[1][k]) and (chr_df['end'][i] >= chr_df2[2][k]))): #both outside
                temp_df=pd.DataFrame(columns=['chr', 'start', 'end', 'gene', 'cnv', 'Pvalue', 'Perc_of_patients', 'Perc_of_controls'])
                temp_df.loc[r, ['chr']]=[chr_df['chr'][i]]
                temp_df.loc[r,['start']] = [chr_df['start'][i]]
                temp_df.loc[r,['end']] = [chr_df['end'][i]]
                temp_df.loc[r,['cnv']] = [chr_df['cnv'][i]]
                temp_df.loc[r,['Pvalue']] = [chr_df['Pvalue'][i]]
                temp_df.loc[r,['Perc_of_patients']] = [chr_df['Perc_of_patients'][i]]
                temp_df.loc[r,['Perc_of_controls']] = [chr_df['Perc_of_controls'][i]]
                temp_df.loc[r,['gene']] = [chr_df2[3][k]]
                new_dfs2.append(temp_df) 
                r=r+1
new_dfs2 = pd.concat(new_dfs2)
final_dfs = new_dfs2    
    
    
for i in range(len(final_dfs['gene'])):
    final_dfs['gene'][i]=final_dfs['gene'][i].split('.')[0]
    
final_dfs = final_dfs.drop_duplicates()





final_dfs = final_dfs.sort_values(by='Pvalue')
final_dfs = final_dfs.reset_index()
final_dfs = final_dfs.drop(columns=['index'])

result_list = []
print("FINAL DF DONE")

for sub_index, sub_frame in final_dfs.groupby('start'): 
    
    first_line = sub_frame.values[0].tolist()
    first_line[3] = ','.join(sub_frame['gene'].tolist())
    
    result_list.append(first_line)

result_frame = pd.DataFrame(result_list, columns=['chr', 'start', 'end', 'gene', 'cnv', 'Pvalue', 'Perc_of_patients', 'Perc_of_controls'])
result_frame = result_frame.sort_values(by='Pvalue')
result_frame.to_csv(sys.argv[5], index=False) ##################### OUTPUT TABLE
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    