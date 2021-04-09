#!/usr/bin/env python
# coding: utf-8

# # Question 2

# <p> Before tackling the problem head on, I wanted to first review the definition given on wikipedia and then make adjustments </p>

# In[1]:


def hamming_distance(string1, string2):
    dist_counter = 0
    for n in range(len(string1)):
        if string1[n] != string2[n]:
            dist_counter += 1
    return dist_counter


# In[2]:


# just trying out two of the test cases from the document
print(hamming_distance('make', 'mage'))
print(hamming_distance('MaiSY', 'MaiZy'))


# \pagebreak

# ## Modification 1
# <p> The first modification to be made is to add another point for capitilization, unless it occurs in the first position </p>

# In[3]:


def hamming_distance1(s1, s2):
    distance = 0
    for n in range(len(s1)):
        if n == 0: # applying a different rule if we are looking at the first position
            if s1[n].lower() != s2[n].lower():
                distance +=1
        else:
            if s1[n].lower() != s2[n].lower(): # modification of original rule
                distance +=1
            
            # The following could be on one line in an or statement, but I visually prefer to see the logic this way
                
            if s1[n].isupper() and s2[n].islower(): # checking for capitilzation and applying excpection
                distance += 0.5
            if s1[n].islower() and s2[n].isupper(): # checking for capitilzation and applying excpection
                distance += 0.5
                
    return distance


# In[4]:


# testing on the exaplmes
print(hamming_distance1('Kitten','kitten'))
print(hamming_distance1('kitten','kiTten'))
print(hamming_distance1('Puppy', 'POppy'))


# \pagebreak

# ## Modification 2
# <p> The second modification considers s and z to be the same letter. The previous rules still apply </p>

# In[5]:


# to make this more dynamic, lets create a list with exceptions that we can add to or remove later
exception_pairs = [('s','z'),('z','s'),('S','Z'),('Z','S')]


# In[6]:


def hamming_distance_Final(s1, s2):
    distance = 0
    for n in range(len(s1)):
        if n == 0:
            if s1[n].lower() != s2[n].lower():
                distance +=1
        else:
            if s1[n].lower() != s2[n].lower():
                if (s1[n],s2[n]) not in exception_pairs: #applying our last exeception
                    distance += 1
            if s1[n].isupper() and s2[n].islower(): 
                distance += 0.5
            if s1[n].islower() and s2[n].isupper():
                distance += 0.5
                
    return distance


# In[7]:


# all text cases explored
print(hamming_distance_Final('make', 'Mage'))
print(hamming_distance_Final('MaiSY', 'MaiZy'))
print(hamming_distance_Final('Eagle','Eager'))
print(hamming_distance_Final('Sentences work too','Sentences wAke too'))


# \pagebreak

# ## Scoring Given Strings

# In[8]:


print('The score for a) is: '+ str(hamming_distance_Final("data Science","Data Sciency")))
print('The score for b) is: '+ str(hamming_distance_Final("organizing","orGanising")))
print('The score for c) is: '
      + str(hamming_distance_Final("AGPRklafsdyweIllIIgEnXuTggzF","AgpRkliFZdiweIllIIgENXUTygSF")))


# ## Applications of Hammering Distance

# <p>One of the applicatins of Hammering Distance I see right away is for spellchecking or spell formatting certain texts. A Hammering Distance above 0 means that that there is something wrong between two texts or two words being compared during a spellcheck algortithim. RegEx can cut through a document and then it can be coupled with this algorithim to give an overall measure of how mispelled a document is. The first exception we made helps when dealing with proper nouns or the beginning of a sentence. The second exception I see as especially useful for comparing US and UK texts, given that we are ignoring the counting for s and z.</p>
