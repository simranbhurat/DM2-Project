#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns


# In[2]:


#%% Importing Datasets
items = pd.read_csv('items.csv', delimiter='|')
orders = pd.read_csv('orders.csv', delimiter='|')
category_hierarchy = pd.read_csv('category_hierarchy.csv', delimiter='|')


# In[3]:


#%%
orders.info()


# In[4]:


#%% Changing the type of the variables
orders['userID'] = orders['userID'].astype(object)
orders['itemID'] = orders['itemID'].astype(object)


# In[5]:


#%% The most preferred products month by month
orders2 = orders
orders2['date'] = pd.to_datetime(orders2['date'])


# In[6]:


#%% Most bought items per month

# June
orders_june = orders2.loc[(orders2['date'] >= "2020-06-01") & (orders2['date'] <= "2020-06-30")]
count = orders_june['itemID'].value_counts()
count = pd.DataFrame(count)
top_10_june =count.head(10)

# July
orders_july = orders2.loc[(orders2['date'] >= "2020-07-01") & (orders2['date'] <= "2020-07-31")]
count2 = orders_july['itemID'].value_counts()
count2 = pd.DataFrame(count2)
top_10_july = count2.head(10)

# August
orders_august = orders2.loc[(orders2['date'] >= "2020-08-01") & (orders2['date'] <= "2020-08-31")]
count3 = orders_august['itemID'].value_counts()
count3 = pd.DataFrame(count3)
top_10_august = count3.head(10)

# September
orders_september = orders2.loc[(orders2['date'] >= "2020-09-01") & (orders2['date'] <= "2020-09-30")]
count4 = orders_september['itemID'].value_counts()
count4 = pd.DataFrame(count4)
top_10_september = count4.head(10)

# October
orders_october = orders2.loc[(orders2['date'] >= "2020-10-01") & (orders2['date'] <= "2020-10-31")]
count5 = orders_october['itemID'].value_counts()
count5 = pd.DataFrame(count5)
top_10_october = count5.head(10)

# November
orders_november = orders2.loc[(orders2['date'] >= "2020-11-01") & (orders2['date'] <= "2020-11-30")]
count6 = orders_november['itemID'].value_counts()
count6 = pd.DataFrame(count6)
top_10_november = count6.head(10)

# December
orders_december = orders2.loc[(orders2['date'] >= "2020-12-01") & (orders2['date'] <= "2020-12-31")]
count7 = orders_december['itemID'].value_counts()
count7 = pd.DataFrame(count7)
top_10_december = count7.head(10)

# January
orders_january = orders2.loc[(orders2['date'] >= "2021-01-01") & (orders2['date'] <= "2021-01-30")]
count8 = orders_january['itemID'].value_counts()
count8 = pd.DataFrame(count8)
top_10_january = count8.head(10)


# In[7]:


#%% JUNE


top_10_june['Category'] =  [
'[2977, 30, 1515, 1760, 2932, 377, 3727, 747, 3915, 3912, 1060, 3268, 2104, 3913, 3935, 4106, 3936, 4113, 3937, 2939, 1395, 1287, 2508, 2925, 888, 3485, 2574, 2844, 2406, 1685, 1002, 2450, 1059, 990, 4006]',
'[1515, 2330, 1760, 3245, 2443, 3173, 3915, 3912, 3914, 1244, 3670, 3457, 1793, 3641]',
'[30, 1515, 1760, 2932, 1287, 2615, 3727, 2450, 990, 1395, 1498, 2654, 3663, 3284, 1060, 3268, 2950, 1179, 278, 2167, 1763, 3935, 3936, 2925, 2844, 377, 2104, 3670, 1482, 3457, 767, 1793, 4114]',
'[836, 2909, 545, 1668, 813, 1515, 3457, 1760, 2083, 2105, 1667, 2975, 744, 278, 3924, 3915, 3912, 3913, 3976, 4008, 3500, 3961, 4104, 4039, 4069, 4119, 664, 392, 4207]',
'[2977, 2844, 1059, 935, 3253, 3113, 990, 1395, 3284, 679, 3945, 3944, 3946, 2939, 3867, 1124, 803, 377, 1685, 1002, 3937]', 
'[2005, 3817, 2205, 2594, 3662, 1000, 2581, 278, 1482, 2167, 3495, 3915, 4030, 2884]',
'[777, 1668, 1390, 3924, 3915, 3912, 3961, 4104, 4207]',
'[74, 3914, 3924, 4048, 3915, 3867, 1124, 803, 3457, 2125, 3546]',
'[74, 3459, 3053, 1763, 3915, 3957, 278, 1482, 2167, 3457, 2929, 4019]',
'[3457, 3693, 2775, 2443, 3173, 3176, 991, 3915, 1763, 3245, 3912, 3914, 3924]']


top_10_june['Brand'] = [
'6',
'18',
'347',
'186',
'6',
'539',
'186',
'186',
'186',
'1496',
]


top_10_june = top_10_june.rename({'itemID': 'Quantity'}, axis=1)
top_10_june = top_10_june.rename_axis('ItemID')


# In[8]:


#%%  JULY


top_10_july['Category'] = [
'[2977, 30, 1515, 1760, 2932, 377, 3727, 747, 3915, 3912, 1060, 3268, 2104, 3913, 3935, 4106, 3936, 4113, 3937, 2939, 1395, 1287, 2508, 2925, 888, 3485, 2574, 2844, 2406, 1685, 1002, 2450, 1059, 990, 4006]',
'[1515, 2330, 1760, 3245, 2443, 3173, 3915, 3912, 3914, 1244, 3670, 3457, 1793, 3641]',
'[777, 1668, 1390, 3924, 3915, 3912, 3961, 4104, 4207]',
'[30, 1515, 1760, 2932, 1287, 2615, 3727, 2450, 990, 1395, 1498, 2654, 3663, 3284, 1060, 3268, 2950, 1179, 278, 2167, 1763, 3935, 3936, 2925, 2844, 377, 2104, 3670, 1482, 3457, 767, 1793, 4114]',
'[836, 2909, 545, 1668, 813, 1515, 3457, 1760, 2083, 2105, 1667, 2975, 744, 278, 3924, 3915, 3912, 3913, 3976, 4008, 3500, 3961, 4104, 4039, 4069, 4119, 664, 392, 4207]',
'[2005, 3817, 2205, 2594, 3662, 1000, 2581, 278, 1482, 2167, 3495, 3915, 4030, 2884]',
'[1986, 795, 30, 1793, 1760, 2083, 1498, 1681, 2654, 3663, 2104, 1763, 4106, 3935, 3937, 1395, 3268, 4113, 990, 3670, 2296, 3457, 3284, 2200]',
'[74, 3914, 3924, 4048, 3915, 3867, 1124, 803, 3457, 2125, 3546]',
'[3457, 3693, 2775, 2443, 3173, 3176, 991, 3915, 1763, 3245, 3912, 3914, 3924]',
'[74, 3459, 3053, 1763, 3915, 3957, 278, 1482, 2167, 3457, 2929, 4019]',
]

top_10_july['Brand'] = [
'6',
'18',
'186',
'347',
'186',
'539',
'703',
'186',
'1496',
'186',
]


top_10_july = top_10_july.rename({'itemID': 'Quantity'}, axis=1)
top_10_july = top_10_july.rename_axis('ItemID')


# In[9]:


#%% AUGUST



top_10_august['Category'] = [
'[1515, 2330, 1760, 3245, 2443, 3173, 3915, 3912, 3914, 1244, 3670, 3457, 1793, 3641]',
'[2977, 30, 1515, 1760, 2932, 377, 3727, 747, 3915, 3912, 1060, 3268, 2104, 3913, 3935, 4106, 3936, 4113, 3937, 2939, 1395, 1287, 2508, 2925, 888, 3485, 2574, 2844, 2406, 1685, 1002, 2450, 1059, 990, 4006]',
'[836, 2909, 545, 1668, 813, 1515, 3457, 1760, 2083, 2105, 1667, 2975, 744, 278, 3924, 3915, 3912, 3913, 3976, 4008, 3500, 3961, 4104, 4039, 4069, 4119, 664, 392, 4207]',
'[74, 3914, 3924, 4048, 3915, 3867, 1124, 803, 3457, 2125, 3546]',
'[74, 3459, 3053, 1763, 3915, 3957, 278, 1482, 2167, 3457, 2929, 4019]',
'[3457, 3693, 2775, 2443, 3173, 3176, 991, 3915, 1763, 3245, 3912, 3914, 3924]',
'[545, 1763, 3912, 3300, 3586, 3914, 3915, 3962, 3963]',
'[1986, 795, 30, 1793, 1760, 2083, 1498, 1681, 2654, 3663, 2104, 1763, 4106, 3935, 3937, 1395, 3268, 4113, 990, 3670, 2296, 3457, 3284, 2200]',
'[30, 1515, 1760, 2932, 1287, 2615, 3727, 2450, 990, 1395, 1498, 2654, 3663, 3284, 1060, 3268, 2950, 1179, 278, 2167, 1763, 3935, 3936, 2925, 2844, 377, 2104, 3670, 1482, 3457, 767, 1793, 4114]',
'[291, 1772, 3540, 1760, 2083, 3038, 1118, 888, 3915, 3882, 4025, 4026, 4068]'

]

top_10_august['Brand'] = [
'18',
'6',
'186',
'186',
'186',
'1496',
'1411',
'703',
'347',
'539'
]


top_10_august = top_10_august.rename({'itemID': 'Quantity'}, axis=1)
top_10_august = top_10_august.rename_axis('ItemID')


# In[10]:


#%% SEPTEMBER



top_10_september['Category'] = [
'[1515, 2330, 1760, 3245, 2443, 3173, 3915, 3912, 3914, 1244, 3670, 3457, 1793, 3641]',
'[2977, 30, 1515, 1760, 2932, 377, 3727, 747, 3915, 3912, 1060, 3268, 2104, 3913, 3935, 4106, 3936, 4113, 3937, 2939, 1395, 1287, 2508, 2925, 888, 3485, 2574, 2844, 2406, 1685, 1002, 2450, 1059, 990, 4006]',
'[836, 2909, 545, 1668, 813, 1515, 3457, 1760, 2083, 2105, 1667, 2975, 744, 278, 3924, 3915, 3912, 3913, 3976, 4008, 3500, 3961, 4104, 4039, 4069, 4119, 664, 392, 4207]',
'[3173, 2775, 3245]',
'[30, 1515, 1760, 2932, 1287, 2615, 3727, 2450, 990, 1395, 1498, 2654, 3663, 3284, 1060, 3268, 2950, 1179, 278, 2167, 1763, 3935, 3936, 2925, 2844, 377, 2104, 3670, 1482, 3457, 767, 1793, 4114]',
'[3457, 3693, 2775, 2443, 3173, 3176, 991, 3915, 1763, 3245, 3912, 3914, 3924]',
'[74, 3914, 3924, 4048, 3915, 3867, 1124, 803, 3457, 2125, 3546]',
'[545, 1763, 3912, 3300, 3586, 3914, 3915, 3962, 3963]',
'[1986, 795, 30, 1793, 1760, 2083, 1498, 1681, 2654, 3663, 2104, 1763, 4106, 3935, 3937, 1395, 3268, 4113, 990, 3670, 2296, 3457, 3284, 2200]',
'[291, 1772, 3540, 1760, 2083, 3038, 1118, 888, 3915, 3882, 4025, 4026, 4068]'
]


top_10_september['Brand'] = [
'18',
'6',
'186',
'1496',
'347',
'1496',
'186',
'1411',
'703',
'539'
]


top_10_september = top_10_september.rename({'itemID': 'Quantity'}, axis=1)
top_10_september = top_10_september.rename_axis('ItemID')


# In[11]:


#%% OCTOBER



top_10_october['Category'] = [
'[1515, 2330, 1760, 3245, 2443, 3173, 3915, 3912, 3914, 1244, 3670, 3457, 1793, 3641]',
'[2977, 30, 1515, 1760, 2932, 377, 3727, 747, 3915, 3912, 1060, 3268, 2104, 3913, 3935, 4106, 3936, 4113, 3937, 2939, 1395, 1287, 2508, 2925, 888, 3485, 2574, 2844, 2406, 1685, 1002, 2450, 1059, 990, 4006]',
'[30, 1515, 1760, 2932, 1287, 2615, 3727, 2450, 990, 1395, 1498, 2654, 3663, 3284, 1060, 3268, 2950, 1179, 278, 2167, 1763, 3935, 3936, 2925, 2844, 377, 2104, 3670, 1482, 3457, 767, 1793, 4114]',
'[3457, 3693, 2775, 2443, 3173, 3176, 991, 3915, 1763, 3245, 3912, 3914, 3924]',
'[74, 3914, 3924, 4048, 3915, 3867, 1124, 803, 3457, 2125, 3546]',
'[1986, 795, 30, 1793, 1760, 2083, 1498, 1681, 2654, 3663, 2104, 1763, 4106, 3935, 3937, 1395, 3268, 4113, 990, 3670, 2296, 3457, 3284, 2200]',
'[545, 1763, 3912, 3300, 3586, 3914, 3915, 3962, 3963]',
'[1515, 2389, 1013, 3693, 2443, 3173, 3625, 2872, 3915, 1763, 2775, 3912, 3914, 1974, 3245, 759, 3924]',
'[3066, 2459, 335, 1515, 450, 1760, 1013, 906, 3263, 3778, 536, 523, 3915, 3914]',
'[2209, 2565, 3173, 3283, 2257, 3409, 278, 3915, 3912, 3913, 3976, 4008, 3914, 3924]'
]


top_10_october['Brand'] = [
'18',
'6',
'347',
'1496',
'186',
'703',
'1411',
'1496',
'267',
'1445'
]


top_10_october = top_10_october.rename({'itemID': 'Quantity'}, axis=1)
top_10_october = top_10_october.rename_axis('ItemID')


# In[12]:


#%% NOVEMBER

top_10_november['Category'] = [
'[1515, 2330, 1760, 3245, 2443, 3173, 3915, 3912, 3914, 1244, 3670, 3457, 1793, 3641]',
'[2977, 30, 1515, 1760, 2932, 377, 3727, 747, 3915, 3912, 1060, 3268, 2104, 3913, 3935, 4106, 3936, 4113, 3937, 2939, 1395, 1287, 2508, 2925, 888, 3485, 2574, 2844, 2406, 1685, 1002, 2450, 1059, 990, 4006]',
'[30, 1515, 1760, 2932, 1287, 2615, 3727, 2450, 990, 1395, 1498, 2654, 3663, 3284, 1060, 3268, 2950, 1179, 278, 2167, 1763, 3935, 3936, 2925, 2844, 377, 2104, 3670, 1482, 3457, 767, 1793, 4114]',
'[3457, 3693, 2775, 2443, 3173, 3176, 991, 3915, 1763, 3245, 3912, 3914, 3924]',
'[74, 3914, 3924, 4048, 3915, 3867, 1124, 803, 3457, 2125, 3546]',
'[1725, 3848, 2921, 2371, 1943, 1763]',
'[545, 1763, 3912, 3300, 3586, 3914, 3915, 3962, 3963]',
'[3173, 2775, 3245]',
'[1986, 795, 30, 1793, 1760, 2083, 1498, 1681, 2654, 3663, 2104, 1763, 4106, 3935, 3937, 1395, 3268, 4113, 990, 3670, 2296, 3457, 3284, 2200]',
'[3066, 2459, 335, 1515, 450, 1760, 1013, 906, 3263, 3778, 536, 523, 3915, 3914]'


]


top_10_november['Brand'] = [
'18',
'6',
'347',
'1496',
'186',
'1324',
'1411',
'1496',
'703',
'267'
]


top_10_november = top_10_november.rename({'itemID': 'Quantity'}, axis=1)
top_10_november = top_10_november.rename_axis('ItemID')


# In[13]:


#%% DECEMBER

top_10_december['Category'] = [
'[1515, 2330, 1760, 3245, 2443, 3173, 3915, 3912, 3914, 1244, 3670, 3457, 1793, 3641]',
'[2977, 30, 1515, 1760, 2932, 377, 3727, 747, 3915, 3912, 1060, 3268, 2104, 3913, 3935, 4106, 3936, 4113, 3937, 2939, 1395, 1287, 2508, 2925, 888, 3485, 2574, 2844, 2406, 1685, 1002, 2450, 1059, 990, 4006]',
'[74, 3914, 3924, 4048, 3915, 3867, 1124, 803, 3457, 2125, 3546]',
'[3457, 3693, 2775, 2443, 3173, 3176, 991, 3915, 1763, 3245, 3912, 3914, 3924]',
'[30, 1515, 1760, 2932, 1287, 2615, 3727, 2450, 990, 1395, 1498, 2654, 3663, 3284, 1060, 3268, 2950, 1179, 278, 2167, 1763, 3935, 3936, 2925, 2844, 377, 2104, 3670, 1482, 3457, 767, 1793, 4114]',
'[545, 1763, 3912, 3300, 3586, 3914, 3915, 3962, 3963]',
'[1986, 795, 30, 1793, 1760, 2083, 1498, 1681, 2654, 3663, 2104, 1763, 4106, 3935, 3937, 1395, 3268, 4113, 990, 3670, 2296, 3457, 3284, 2200]',
'[3173, 2775, 3245]',
'[1515, 2389, 1013, 3693, 2443, 3173, 3625, 2872, 3915, 1763, 2775, 3912, 3914, 1974, 3245, 759, 3924]',
'[3066, 2459, 335, 1515, 450, 1760, 1013, 906, 3263, 3778, 536, 523, 3915, 3914]'
]


top_10_december['Brand'] = [
'18',
'6',
'186',
'1496',
'347',
'1411',
'703',
'1496',
'1496',
'267'
]


top_10_december = top_10_december.rename({'itemID': 'Quantity'}, axis=1)
top_10_december = top_10_december.rename_axis('ItemID')


# In[14]:


#%% JANUARY

top_10_january['Category'] = [
'[1515, 2330, 1760, 3245, 2443, 3173, 3915, 3912, 3914, 1244, 3670, 3457, 1793, 3641]',
'[2977, 30, 1515, 1760, 2932, 377, 3727, 747, 3915, 3912, 1060, 3268, 2104, 3913, 3935, 4106, 3936, 4113, 3937, 2939, 1395, 1287, 2508, 2925, 888, 3485, 2574, 2844, 2406, 1685, 1002, 2450, 1059, 990, 4006]',
'[74, 3914, 3924, 4048, 3915, 3867, 1124, 803, 3457, 2125, 3546]',
'[3901, 3900, 3903, 3916, 1110, 766]',
'[3457, 3693, 2775, 2443, 3173, 3176, 991, 3915, 1763, 3245, 3912, 3914, 3924]',
'[1110]',
'[30, 1515, 1760, 2932, 1287, 2615, 3727, 2450, 990, 1395, 1498, 2654, 3663, 3284, 1060, 3268, 2950, 1179, 278, 2167, 1763, 3935, 3936, 2925, 2844, 377, 2104, 3670, 1482, 3457, 767, 1793, 4114]',
'[3429, 2872, 694]',
'[545, 1763, 3912, 3300, 3586, 3914, 3915, 3962, 3963]',
'[2315, 3429, 381, 535, 3283]'

]


top_10_january['Brand'] = [
'18',
'6',
'186',
'105',
'1496',
'1445',
'347',
'1055',
'1411',
'1445'

]


top_10_january = top_10_january.rename({'itemID': 'Quantity'}, axis=1)
top_10_january = top_10_january.rename_axis('ItemID')


# In[15]:


#%%
top_10_june


# In[17]:


#%%
top_10_july


# In[18]:


#%%
top_10_august


# In[19]:


#%%
top_10_september


# In[20]:


#%%
top_10_october


# In[21]:


#%%
top_10_november


# In[22]:


#%%
top_10_december


# In[23]:


#%%
top_10_january


# Items 18630, 29657 & 20131 are almost always in top 3. 
# Together with those three items, 16059, 11251, 1970 & 23050 are
# always in the list of top 10 for every month. The brand of the every
# item is different. 
# 
# For the always top three items, Matched category: 1515 & 1760.
# 
# But still, during june, 129924 different items are bought by people.
# Top 10 doesn't even represent 10000 people. There are a lot
# of different items. Focusing on categories may make sense. 
# 
# Eventhough 19267, 17419 & 32204 aren't sold in the June-July-August-September,
# they were sol in top 10 after October. But still, they weren't big numbers. 
# 
# As a brand, 18, 6 & 186 were always in top 3. 

# In[24]:


#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns


# In[25]:


#%% Top 10 Items purchased by customerss in dataset

plt.figure(figsize=(15,5))
sns.barplot(x = orders.itemID.value_counts().head(10).index, y = orders.itemID.value_counts().head(10).values, palette = 'gnuplot')
plt.xlabel('Items', size = 15)
plt.xticks(rotation=45)
plt.ylabel('Count of Items', size = 15)
plt.title('Top 10 Items purchased by customers', color = 'black', size = 20)
plt.show()


# In[26]:


#%% Extracting month and replacing it with text
orders['date'] = pd.to_datetime(orders['date'])

orders['month'] = orders['date'].dt.month
orders['month'] = orders['month'].replace((1,6,7,8,9,10,11,12), 
                                          ('January','June','July','August',
                                          'September','October','November','December'))

# Extracting weekday and replacing it with text
orders['weekday'] = orders['date'].dt.weekday
orders['weekday'] = orders['weekday'].replace((0,1,2,3,4,5,6), 
                                          ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'))


# In[27]:


#%% order by day
weekTran = orders.groupby('weekday')['order'].count().reset_index()
weekTran.loc[:,"weekorder"] = [4,0,5,6,3,1,2]
weekTran.sort_values("weekorder",inplace=True)

plt.figure(figsize=(12,5))
sns.barplot(data = weekTran, x = "weekday", y = "order")
plt.xlabel('Week Day', size = 15)
plt.ylabel('Orders per day', size = 15)
plt.title('Number of orders received each day', color = 'green', size = 20)
plt.show()


plt.show()


# In[28]:


#%% order by month
monthTran = orders.groupby('month')['order'].count().reset_index()
monthTran.loc[:,"monthorder"] = [4,8,12,2,1,7,6,3]
monthTran.sort_values("monthorder",inplace=True)

plt.figure(figsize=(12,5))
sns.barplot(data = monthTran, x = "month", y = "order")
plt.xlabel('Months', size = 15)
plt.ylabel('Orders per month', size = 15)
plt.title('Number of orders received each month', color = 'green', size = 20)
plt.show()


plt.show()


# Apriori Algorithm part comes from R-Studio. Find it in Github R.Markdown
