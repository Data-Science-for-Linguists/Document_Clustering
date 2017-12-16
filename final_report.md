Daniel Zheng, [daniel.zheng@pitt.edu](mailto:daniel.zheng@pitt.edu)
# Automatic Bookmark Organizing with Document Clustering
### Table of Contents
- [Introduction](#introduction)
- [Data](#data)
  - [License](#license)
  - [Preprocessing](#preprocessing)
- [Clustering](#clustering)
  - [K-means](#k-means)
    - [Labeling](#labeling)
  - Agglomerative
    - Labeling
- Discussion
- Future Work
- References

## Introduction
This project began when I realized that my browser's bookmarks bar was a mess and desired a way to automatically clean it up. Whenever I come across an interesting webpage, I immediately bookmark it. However, over the years, I've stopped properly organizing these bookmarks and placing them into appropriate folders, instead leaving them just as links, not even contained in a single folder. At the far right of my bookmarks bar is a `>>` icon, which expands into a horrifyingly long list of hundreds of URLs when clicked. Undoubtedly, many, if not all of these links contain interesting and useful information, but they are so disorganized that it is essentially impossible for me to ever find what I'm looking for.

For my term project in LING1340, I initially thought it would be interesting to create a Chrome extension that takes list of bookmarks (URLs), automatically clusters them into folders, and rearranges the bookmarks bar, solving my problem.

This would entail:
- Learning Chrome's bookmarks API and making the extension
- Hierarchical clustering
- Cluster labeling (folder names)

Since the class is about natural language processing, I chose to focus on investigating clustering and labeling for this project.

## Data
I did not want to publicly share my own bookmarks list for privacy reasons, so I began by accumulating a list of news articles and other webpages through web scraping with `BeautifulSoup`, stripping HTML tags and removing JavaScript code to extract text that was representative of the contents of each page. Though this is closest to the initial bookmark organizing project I described, it was tedious and difficult to compile a large dataset by hand. As a simplification, I chose to use a Wikipedia dump. Because the clustering algorithms I'm investigating are completely unsupervised, it shouldn't matter what kind of data they are run on. I also chose Wikipedia because Wikipedia articles have very clear and focused topics, ideal for clustering algorithms.

### License
Wikipedia is licensed under CC-BY-SA according to [this page](https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content), which requires me to distribute resulting work under a similar license. Accordingly, my repository is licensed under GPLv3.

### Preprocessing
The Wikipedia data was initially in an extremely unwieldy XML format. Luckily, I was able to find the [Wikiextractor](https://github.com/attardi/wikiextractor/) library that I used to convert my into a much more manageable JSON format, saving `title, url, text`, and `id` for each article. This saved each article on one line, so I performed some further processing myself to save all articles in a file into one list.

## Clustering
With my data in hand, I began to read about clustering. I quickly learned that there are two main types of clustering, K-means and Hierarchical. While hierarchical clustering seemed more suitable for my bookmark organizing problem, as it organizes things into clusters and sub-cluster, K-means was more intuitive and simpler to understand. For this reason, I chose to first look at K-means clustering.

### K-means
The K-means clustering algorithm aims to produce *k* clusters by finding *k* centroids and a label for each data point, so that each point belongs to the cluster with the nearest centroid, or mean.

First, initialize the centroids. There are a variety of ways to do this that can speed the algorithm up, but for simplicity let's assume random initialization.

The main algorithm consists of two repeated steps.
1. For each point, calculate the Euclidean distance in the feature space to each centroid, assigning it to the closest one.
2. Recalculate the centroids to be the averages of the points in each current cluster.
3. Repeat steps 1 and 2 until there are no longer any changes in the centroids.

Below is a graphic from [this page](http://www.learnbymarketing.com/methods/k-means-clustering/) that shows K-means in action.
![png](img/k-means-steps-example.png)
