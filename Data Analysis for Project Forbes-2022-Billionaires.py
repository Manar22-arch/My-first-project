#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy  as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
sns.set_theme(rc={'figure.figsize':(8, 8)}, font_scale=1.3)
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[21]:


df = pd.read_csv(r"E:\AI from A to Z Course\Python for DA & AI\Session 04\Project 2\Forbes-2022-Billionaires-db.csv",
                 encoding="latin-1") #utf-8


# In[22]:


df.head()


# In[17]:


df.tail()


# In[18]:


df.sample(5)


# In[19]:


df.info()


# In[20]:


df.shape


# In[21]:


df.describe()


# In[22]:


df.describe(include='object')


# In[23]:


df.isnull().sum().sort_values(ascending=False)


# In[24]:


for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{}  -  {}%'.format(col, round(pct_missing*100)))


# In[25]:


for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    pct_missing =  round(pct_missing*100)
    if pct_missing >= 30 :
      df.drop([col],axis = 1,inplace = True)
      print('Droping {} Column as it contain - {}% null values'.format(col, pct_missing))


# In[26]:


df.shape


# In[27]:


for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{}  -  {}%'.format(col, round(pct_missing*100)))


# In[28]:


for column in df.columns:
    if df[column].dtype == 'object':  
        df[column] = df[column].fillna(df[column].mode()[0])
    elif df[column].dtype in ['int64', 'float64']:  
        df[column] = df[column].fillna(df[column].mean())


# In[29]:


df.isnull().sum()


# In[30]:


df.head()


# In[32]:


columns_drop = 'source '.split()
columns_drop


# In[33]:


df.drop(columns_drop,axis=1,inplace=True)


# In[34]:


df.shape


# We start with 22 columns after droping columns that contain 30% null values or more and anthor columns that aren't important , we finally has 14 columns

# In[36]:


df.info()


# In[37]:


df.columns


# Top 10 Forbes-2022-Billionaires in the world

# In[38]:


top_10_name= df['personName'].value_counts().head(10)
top_10_name


# In[39]:


top_10_name.index


# In[42]:


plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_name.values, y=top_10_name.index, palette="coolwarm")
plt.title("Top 10 Forbes-2022-Billionaires in the world", size=16)
plt.xlabel("Names", size=14)
plt.ylabel("finalWorth", size=14)
plt.savefig('top_10_Forbes.png')
plt.show()


# Gender of Forbes-2022-Billionaires in the world (Male or Female)

# In[60]:


df['gender'] = df['gender'].str.strip() # حذف المسافات الزائدة

#df['gender_label'] = df['gender'].map({'M': "Male", 'F': "Female"})


# In[61]:


df.head()


# In[65]:


sns.countplot(x = df['gender_label'],order = df['gender_label'].value_counts().index)
plt.title("Male or Female of Forbes-2022-Billionaires ", size=20)
plt.show()


# In[64]:


plt.figure(figsize=(12,8))
plt.pie(df['gender_label'].value_counts(),labels=['Male','Female'],
        autopct ='%1.2f%%',shadow = True, explode = [0,0.1],colors = ['r','b'])
plt.title("Male or Female of Forbes-2022-Billionaires ", size=20)
plt.legend(loc = 'upper right')
plt.show()


# **Insight:The chart clearly shows that the city  of Forbes-2022-Billionaires 

# Forbes-2022-Billionaires and their city
# 

# For City

# In[67]:


df['city'].value_counts()


# In[76]:


# 1. ضبط الحجم ليكون متناسقاً (ليس ضخماً جداً)
sns.set_theme(rc={'figure.figsize':(12, 7)}, font_scale=1.1)

# 2. أخذ عينة محددة (أول 10 مدن مثلاً) لتظهر الأعمدة كبيرة
data_to_plot = df['city'].value_counts().head(10)

# 3. الرسم مع زيادة عرض العمود (width)
plt.bar(data_to_plot.index, data_to_plot.values, 
        facecolor='pink', edgecolor='blue', width=0.6) # تقليل الـ width يجعلها أعرض بصرياً بالنسبة للمساحة

plt.title("Top 10 Cities in Forbes 2022", size=20)
plt.xticks(rotation=45) # تدوير الأسماء لكي لا تتداخل
plt.ylabel("Number of Billionaires")

plt.show()


# In[25]:


plt.figure(figsize=(15, 8))
sns.boxplot(data=df, x='category', y='finalWorth', palette='viridis')
plt.title("Wealth Distribution by Industry Category", size=20)
plt.xticks(rotation=45, ha='right')
plt.show()


# In[28]:


sns.set_theme(rc={'figure.figsize':(15, 10)}, font_scale=1)
plt.title(" Top 10 Cities in Forbes 2022  ", size=20)
plt.bar(df['city'].value_counts().head(10).index,df['city'].value_counts().head(10),
        facecolor='r',edgecolor='b')
plt.show()


# New York City has consistently been the primary hub for the world’s wealthiest individuals, maintaining the highest concentration of billionaires for decades."

# In[41]:


sns.set_theme(rc={'figure.figsize':(20, 10)}, font_scale=1.4)


df.groupby('age')['finalWorth'].count().plot(color='b', ls='-', lw=8, alpha=0.85)

plt.title("Billionaire Distribution Growth by age", size=26)
plt.xlabel('age', color='k', size=20) 
plt.ylabel('Number of Billionaires', color='k', size=20) 

plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# In[34]:


print(df.columns)


# In[ ]:




