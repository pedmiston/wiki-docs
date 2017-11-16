# Wikipedia

`{{NUMBEROFARTICLES}}`

[Wikipedia statistics](https://en.wikipedia.org/wiki/WP:ST)

## wiki syntax

[Example article](https://en.wikipedia.org/wiki/Persoonia_terminalis)  
[Mediawiki doc page for wiki syntax](https://www.mediawiki.org/wiki/Help:Formatting)

## wiki is a markup language

Other markup languages:

- Markdown
- Github flavored Markdown
- CommonMark
- **Rmarkdown**
- ReStructuredText

_Markup languages are the engine that powers dynamic documents._

## Links

```
# markdown
[Persoonia terminalis](https://en.wikipedia.org/wiki/Persoonia_terminalis) was the 5 millionth article to be published on the English Wikipedia.

# rst
`Persoonia terminalis
<https://en.wikipedia.org/wiki/Persoonia_terminalis>`_ was the 5 millionth article to be published on the English Wikipedia.

`Persoonia terminalis`_ was the 5 millionth article to be published on the English Wikipedia.

.. _`Persoonia terminalis`: https://en.wikipedia.org/wiki/Persoonia_terminalis

# wiki
[[Persoonia terminalis]] was the 5 millionth article to be published on the English Wikipedia.

[[Persoonia terminalis|An article on a shrub native to eastern Australia]] was the 5 millionth article to be published on the English Wikipedia.
```

## Images

```
# markdown
![Persoonia terminalis](images/Persoonia_terminalis.jpg)

# rst
.. image: images/Persoonia_terminalis.jpg

# wiki
[[File:Persoonia_terminalis.jpg]]
```

_Markup languages allow you to include images without clicking._

## Templates

```
# markdown
NA!

# rst
|RST| is a little annoying to type over and over, especially
when writing about |RST| itself, and spelling out the
bicapitalized word |RST| every time isn't really necessary for
|RST| source readability.

.. |RST| replace:: reStructuredText

# wiki
There are {{NUMBEROFARTICLES}} English Wikipedia articles.

# Rmd
There are `r num_articles` English Wikipedia articles.
```

## Infoboxes

[List of infoboxes](https://en.wikipedia.org/wiki/Wikipedia:List_of_infoboxes)  
[Transclusion](https://en.wikipedia.org/wiki/Wikipedia:Transclusion)

## Wikidata

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">77% of Catalan <a href="https://twitter.com/Wikipedia?ref_src=twsrc%5Etfw">@wikipedia</a> articles use automated info from <a href="https://twitter.com/wikidata?ref_src=twsrc%5Etfw">@wikidata</a> <br>39% of articles have infoboxes fully powered by <a href="https://twitter.com/wikidata?ref_src=twsrc%5Etfw">@wikidata</a> 😎 <a href="https://t.co/t6Yk5xFEDN">https://t.co/t6Yk5xFEDN</a></p>&mdash; Àlex Hinojo (@AlexHinojo) <a href="https://twitter.com/AlexHinojo/status/928704158252838912?ref_src=twsrc%5Etfw">November 9, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

[Wikitribune story about Wikidata](https://beta.wikitribune.com/story/2017/11/10/tech/internet-tech/wikidata-a-growing-community-behind-open-data/17923/)
