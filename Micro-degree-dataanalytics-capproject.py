#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


df=pd.read_csv("C:\Invideos.csv")
print(df)


# In[7]:


df.columns



# In[8]:


df.isnull().any()


# In[10]:


df["description"]=df["description"].fillna(value="")


# In[11]:


df.isnull().any()


# In[20]:


#Which year was data collected....


# In[26]:


cdf=(df['trending_date'].apply(lambda x: '20'+x[:2]).value_counts().to_frame().reset_index().rename(columns={"index":"year","trending_date":"no_of_videos"}))


# In[27]:


print(cdf)


# In[28]:


plt.bar(cdf['year'],cdf['no_of_videos'])


# In[30]:


#what is the percentage of videos released in that particular year
df['trending_date'].apply(lambda x: '20'+x[:2]).value_counts(normalize=True)


# In[31]:


df.describe()


# In[32]:


df.hist('views')


# In[35]:


#percentage of videos less than 1 million views
df[df['views']<1e6]['views'].count()/df['views'].count()*100


# In[34]:


#number of videos greater than 1 million views
df[df['views']<1e6]['views'].count()


# In[36]:


df.hist('likes')


# In[37]:


#percentage of likes greater than 50k likes
df[df['likes']>50000]['likes'].count()/df['likes'].count()*100


# In[42]:


#descripion of non-numerical columns

df.describe(include = 'O')


# In[44]:


#calculate title lenght & adding new column
df['title_len']=df['title'].apply(lambda x: len(x))


# In[45]:


df.columns


# In[46]:


df.head(5)


# In[52]:


df.boxplot('title_len')


# In[55]:


#is there any relation between title lenght & no of vidoes

plt.scatter(df['title_len'],df['views'])


# In[56]:


df.corr()


# In[58]:


#group data based on category ID
df.groupby('category_id').sum()


# In[61]:


#category with highest views

plt.bar(df['category_id'],df['views'])


# In[62]:


#category with highest likes

plt.bar(df['category_id'],df['likes'])


# In[63]:


df.info()


# In[64]:


#how many videos had some error
df['video_error_or_removed'].value_counts()


# In[65]:


#videos that have comments disabled
df['comments_disabled'].value_counts(normalize=True)


# In[67]:


#how many videos have both comments and ratings disablled

len(df[(df['comments_disabled']==True) & (df['ratings_disabled']==True).index])


# In[ ]:




