#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install textblob')


# In[2]:


from textblob import TextBlob


# In[3]:


f = open("news.txt")


# In[4]:


d = f.read()


# In[5]:


print(d)


# In[6]:


TextBlob(d).sentiment


# In[ ]:




