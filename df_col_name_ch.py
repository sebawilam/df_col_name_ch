# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 12:24:13 2022

@author: wilamowsse01
"""

import pandas as pd

# create dictonary lists
dict_of_list = {
    'level1:123' : ['afdfnd', 'gdghekjw'],
    'level2:456' : ['geheg', 'ghdlgee'],
    'level3:789' : [123, 987]
}

# create df from dictonary lists
df = pd.DataFrame(dict_of_list)
print(df)

# change all names using the loop
for col in df.columns: 
    new_col = col[0:6]
    df.rename(columns = {col:new_col},inplace = True)
print(df)

print(df.sample())
