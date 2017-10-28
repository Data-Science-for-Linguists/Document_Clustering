# Term Project Progress Log

## 10/27/2017
Slight change of plans. Originally, I wanted to have the user define the max folder size that would be used to split folders into subfolders if they are too big. However I think now I'm going to :
- Use some unsupervised method to create groups and subgroups
- Provide a simple method to add new documents, as clustering is expensive and slow.

## 10/08/2017
Added jupyter notebook. Since my data will be list of URLs (eventually 1000s of them), I wrote a simple function to strip out tags and leave the page text. I also experimented with the Wikipedia API. The main challenge for my project is clustering and measuring semantic distances, both of which I don't know how to do. So for now, I'm focusing on figuring out gensim and word2vec, etc with a dummy list of 4 wikipedia pages.

## 9/30/17
Created project repo and added plan, progress report, license, and readme.
