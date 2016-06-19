# django-silly-search

Simple django-app for search by Q-expressions.

[![Build Status](https://travis-ci.org/Egregors/django-silly-search.svg?branch=master)](https://travis-ci.org/Egregors/django-silly-search)

If you need the simple way to search, without full-text,
morphology features, this app may be useful. But, if you need search for more
complicated case, you should use something like [Haystack](http://haystacksearch.org/)

## Features

* Search for one or few models
* Search for multiple fields

## Install

Clone this repo and install from the source:
```
git clone https://github.com/Egregors/django-silly-search.git
cd django-silly-search
pip install -e .
```

or just use PyPI

```
pip install django-silly-search
```

## How to use

The app provides a single function:

```
from silly_search import q_search

# q_search(models, fields, q) -> list of ModelBase instances
```
The functions takes required arguments:

`models` – Models for search. Should be instance of `ModelBase` (regular Model)
or `list` of `ModelBase` instances

`fields` – Fields for search. Should be `str` or `list` of `str` (just name of models field)

`q` – phrase for search. Should be an `str`

As result, you'll get list of ModelBase instances.
Keep in mind, if you use it to search for few different models, you'll probably get
list of instances different ModelBase class heirs.

## Example

Let's say you have Models:

```
class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    text = models.TextField()


class News(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()Z
```

and you want to make search on these models. So, you can search for one model and one field:

```
    q_search(Article, 'title', q='spam')
```

or for one models, but few fields:

```
    q_search(Article, fields=['title', 'text'], q='spam')
```

or for few models and few fields:
```
    q_search(models=[Article, News], fields=['title', 'description', 'text'], q='spam')
```

## Contributing

Bug reports, bug fixes, and new features are always welcome.
Please open issues, and submit pull requests for any new code.