# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:04:20 2023

@author: peded
"""

####### Libraries #######

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



####### Declarations of objects #######

df = pd.read_csv('C:/Users/peded/Desktop/Davide/Documenti/FILE CSV/GamingStudy_data.csv')
avr_age = df['Age'].mean() 
avr_gad = df['GAD_T'].mean()
gad = df['GAD_T']
gen_distr = df['Gender'].value_counts(normalize=True) * 100
deg_distr = df['Degree'].value_counts(normalize=True) * 100
occ_distr = df['Work'].value_counts(normalize=True) * 100
plat_distr = df['Platform'].value_counts(normalize=True) * 100
vg_distr = df['Game'].value_counts(normalize=True) * 100
nat_distr = df['Residence'].value_counts(normalize=True) * 100


####### Rounding the values and adding the char "%" at the end of every percentile value #######


avr_age = avr_age.round(2)
avr_gad = avr_gad.round(2)
gen_distr = gen_distr.round(2).astype(str) + " %"
deg_distr = deg_distr.round(2).astype(str) + " %"
occ_distr = occ_distr.round(2).astype(str) + " %"
plat_distr = plat_distr.round(2).astype(str) + " %"
vg_distr = vg_distr.round(2).astype(str) + " %"
nat_distr = nat_distr.round(2).astype(str) + " %"
nat_distr = nat_distr.head(10)    


####### Prints the messages and the values on Console #######

print('\n'"THE AVERAGE AGE IS =",avr_age)
print('\n'"THE AVERAGE GAD IS =",avr_gad,'\n')
print('\n'"THE GENDER DISTRIBUTION IS ="'\n\n',gen_distr,'\n\n')
print('\n'"THE DEGREE DISTRIBUTION IS ="'\n\n',deg_distr,'\n\n')
print('\n'"THE OCCUPATION DISTRIBUTION IS ="'\n\n',occ_distr,'\n\n')
print('\n'"THE PLATFORM DISTRIBUTION IS ="'\n\n',plat_distr,'\n\n')
print('\n'"THE GAMES DISTRIBUTION IS ="'\n\n',vg_distr,'\n\n')
print('\n'"THE TOP 10 COUNTRIES ARE ="'\n\n',nat_distr,'\n\n')



####### Plots #######

#df.plot(kind = 'scatter' , x = 'GAD_T' , y = 'Platform')
plt.figure()
sns.histplot(gad, bins=21, color='purple', label = 'GAD_total' )
plt.show()