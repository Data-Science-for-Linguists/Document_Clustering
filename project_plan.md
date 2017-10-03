### Project Ideas:

#### 1. Scraping bookmarks from Chrome, automatically group bookmarks into folders and subfolders with topic modeling. In a more general sense, this will group a list of URLs into topics and subtopics.

*Data*:
- A list of URLs to articles
- Each page will need to be cleaned from the page source code into a nice block of text (HTML parser libraries exist, but inline javascript will need to be handled somehow). 

*Analysis*:
- Using a list of URLs, it's possible to extract some interesting linguistic insights to understand what the user is interested in. 
- Gensim for topic modeling, keras/sci-kit for any ML. 
- Can generate a summary about each article/URL about sentence length, TTR, and stuff as well as an actual summary of maybe 3-4 important sentences extracted from the article (textrank?).
- Some kind of ML may need to be employed to group things by their topics, because it's really hard to programmatically know that an article about apples and another about oranges should go a folder called "Fruit". Really unsure about a good approach for this.

*Presentation*
- Could turn into a python module or even a package
- Test on my own bookmarks, or some giant list of URLs and see how it turns out.
