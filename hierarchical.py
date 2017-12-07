
# coding: utf-8

# Helpful resource: http://brandonrose.org/clustering
# 
# 

# In[25]:


#%matplotlib notebook


# In[26]:


import json
import glob
import random

wiki_articles = []
for x in glob.glob('data/wiki*.json'):
    new_articles = json.load(open(x))['articles']
    wiki_articles += new_articles
wiki_articles[0].keys()
wiki_articles = random.sample(wiki_articles, len(wiki_articles)//2)


# In[27]:


from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_df=0.8, max_features=20000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, ngram_range=(1,3))
wiki_articles_text = [x['text'] for x in wiki_articles]
wiki_articles_titles = [x['title'] for x in wiki_articles]
tfidf_vectors = tfidf.fit_transform(wiki_articles_text)


# In[34]:


from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
dist = 1 - cosine_similarity(tfidf_vectors)


# In[35]:


import matplotlib
matplotlib.rcParams.update({'font.size': 12})

linkage_matrix = ward(dist) #define the linkage_matrix using ward clustering pre-computed distances

fig, ax = plt.subplots(figsize=(15, 20)) # set size
ax = dendrogram(linkage_matrix, orientation="right", labels=wiki_articles_titles);

plt.tick_params(    axis= 'x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off')

#plt.tight_layout() #show plot with tight layout
plt.show()

