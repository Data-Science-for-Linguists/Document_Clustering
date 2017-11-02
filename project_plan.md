### Project Ideas:

#### Document Clustering

*Data*:
- A corpus of wikipedia articles and potentially other corpora (but wikipedia is massive and very good for topic modeling).
- I'm no longer web scraping. Instead, I've downloaded a dump of wikipedia (very large) that I'm storing locally.
- A sample of a few pages of the dump in JSON format will be included in the `data/` folder.

*Analysis*:
- Visualization with t-SNE and some kind of interesting graphical representation
- Document clustering using Kullback-Leibler divergence is the plan.
- Instead of reclustering on the introduction of a new input, I can turn it into classification?
  - Or maybe have both as options
- End goal is a python package to cluster input text documents and visualize the result.
- Will try to implement some things myself (for learning purposes).
- Maybe I can improve the clusters after the original clustering using reinforcement learning with user input.
- Can compare to other document clustering algorithms

*Presentation*
- Jupyter notebooks for a majority of the code, writeups will be in markdown/latex 
