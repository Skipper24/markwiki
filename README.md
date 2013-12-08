MarkWiki
========

[![PyPI version][fury]](http://badge.fury.io/py/MarkWiki)
[![Downloads][pypip]](https://crate.io/packages/MarkWiki)
[![Build Status][travis]](https://travis-ci.org/mblayman/markwiki)

*A simple wiki using Markdown*

The user documentation for MarkWiki is at http://pythonhosted.org/MarkWiki/.

Design Goal
-----------

MarkWiki should be as simple as possible to set up. A basic working
configuration should never need more than two steps.

1.  Install.
2.  Start.

Why? MarkWiki is aimed at teams that want a no fuss, no frills wiki. Simplicity
trumps features.

Contributing
------------

Fork MarkWiki on GitHub and submit a pull request when you're ready.

Additional guidance is available in the developer documentation at
[Read the Docs][rtd].

Running MarkWiki
----------------

### Users

From a command line, run:

```bash
$ pip install MarkWiki
$ markwiki
```

### Developers

From the project's root directory, run:

```bash
$ pip install -r requirements.txt
$ python setup.py develop
$ markwiki
```

This will do three things for developers: install the *exact* versions used by
other developers, install the `markwiki` console script, start MarkWiki.

[fury]: https://badge.fury.io/py/MarkWiki.png
[pypip]: https://pypip.in/d/MarkWiki/badge.png
[travis]: https://travis-ci.org/mblayman/markwiki.png?branch=master
[rtd]: http://markwiki.readthedocs.org/en/latest/contribute.html
