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

This would be a rather involved task, however, so I chose to focus on investigating clustering and labeling for this project.

## Data
I did not want to publicly share my own bookmarks list for privacy reasons, so I began by accumulating a list of news articles and other webpages through web scraping with `BeautifulSoup`, stripping HTML tags and removing JavaScript code to extract text that was representative of the contents of each page. Though this is closest to the initial bookmark organizing project I described, it was tedious and difficult to compile a large dataset by hand. As a simplification, I chose to use a Wikipedia dump. Because the clustering algorithms I'm investigating are completely unsupervised, it shouldn't matter what kind of data they are run on. I also chose Wikipedia because Wikipedia articles have very clear and focused topics, ideal for clustering algorithms.
### License
