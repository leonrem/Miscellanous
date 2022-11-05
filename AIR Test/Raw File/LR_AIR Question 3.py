#!/usr/bin/env python
# coding: utf-8

# # Question 3

# <p>Before taking on this question, I will import pandas to help me work with the csv dataset.</p>

# In[1]:


import pandas as pd


# In[2]:


# I kept the csv in the same directory as this file
patents = pd.read_csv('patent_drawing.csv') 


# In[3]:


# I take a quick peak at how the information came in
patents.head()


# ## Part A

# <p>Hopefully I am understanding this question correctly. It seems like we want to see how many rows have the word(s) "view" or "perspective" in them while not including those rows which also have "bottom", "top", "front" or "rear" in the text field.</p>

# In[4]:


# To make this more dynamic, I make a list of what we want to find and what we want to avoid
target_words = ['view', 'perspective']
avoid_words = ['bottom','top','front','rear']


# \pagebreak

# In[5]:


count = 0

for s in patents['text']: # parsing through each description
    split_text = s.split() # splitting each text by a whitespace, because words like 'ontop' should not flag
    flag = 0
    for a in avoid_words: # comparing each of the words we want to avoid with the text
        if a in split_text: 
            flag += 1 # if a word we should avoid is found in the text, we flag it to move to a new text
            break
    if flag < 1: # testing to see if our first search flagged
        for t in target_words: # following the same setup as in our first test
            if t in split_text: 
                count+=1
    else:
        pass # if the flag is raised, we move on to the next text line
    
print('The number of text entries that include \"view\" or \"perspective\" but ' 
      + str('not \"bottom\", \"top\", \"front\", or \"rear\" is: ')+ str(count))


# ## Part B

# <p>Because some of the patent_ids are strings, it is harder to groupby patent_id. So we need to understand how the patent_id data looks like.</p>

# In[6]:


patents['patent_id'].describe()


# <p>The simple description actually allows us to understand how to calculate the average number of pictures per patent. We will take the total number of entries and divide by the number of uniquie entries.</p>

# In[7]:


avg = len(patents.index)/patents['patent_id'].nunique()

print('The average number of pictures per patent is: '+ str(avg))

