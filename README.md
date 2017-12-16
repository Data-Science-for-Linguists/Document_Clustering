# Automatic Bookmark Organizing with Document Clustering.
Daniel Zheng, [daniel.zheng@pitt.edu](mailto:daniel.zheng@pitt.edu)

Originally, I wanted to create a way to automatically clean up my bookmarks bar. I have hundreds, maybe thousands of bookmarks floating around not sorted into their proper folders.

I then thought, it would be cool to make a Chrome extension that takes list of bookmarks
(URLs), automatically clusters them into folders, and rearranges your bookmarks bar!

This would entail:
- Learning Chrome's bookmarks API and making the extension
- Hierarchical clustering
- Cluster labeling (folder names)

For this project, I decided to focus on clustering and labeling. K-means and Hierarchical methods were investigated.

## Dataset
For this project, I utilized a 12GB text dump of wikipedia found [here](https://dumps.wikimedia.org/backup-index.html). Since the clustering is unsupervised, it isn't necessary to run the algorithms on the entire dataset, though I eventually will do so. In the [data](data) folder are a small sample of JSON files of wikipedia articles.



### Repository Contents
- [Practicing topic extraction](project_old.ipynb)
- [Visitor log](https://github.com/Data-Science-for-Linguists/Shared-Repo/blob/master/todo10_visitors_log/visitors_log_dan.md)
- [Final Report](final_report.md)
- K-means Clustering and Visualization
  - [Jupyter Notebook](clustering.ipynb)
  - [Markdown](clustering.md)
- Hierarchical Clustering and Visualization
  - [Jupyter Notebook](hierarchical.ipynb)
  - [Markdown](hierarchical.md)
- [Class Presentation Slides](ling1340_slides.pdf)
- [Data](data), JSON files of wikipedia articles
- [Images](img), folder of all images used in repository
- [Cluster Pickle Files](clusters), saved `.pkl` files of clustering outputs
- Preprocessing
  - [Wikiextractor](wikiextractor), a submodule of the repo used in converting wikipedia XML dump to json
  - [Reformatting Script](reformat.py), a short custom script for some further preprocessing to convert from JSON Lines format into one dict per file.

NOTE: Before running any of this code, I would recommend installing all dependencies with `pip install -r requirements.txt`.
