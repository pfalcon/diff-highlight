.. image:: https://travis-ci.org/pfalcon/diff-hilite.svg?branch=master
   :target: https://travis-ci.org/pfalcon/diff-hilite

.. image:: https://coveralls.io/repos/pfalcon/diff-hilite/badge.png?branch=master
   :target: https://coveralls.io/r/pfalcon/diff-hilite?branch=master

***************************************************************
diff-hilite - Highlight intra-line differences in "diff" output
***************************************************************

``diff-hilite`` adds intra-line differences highlighting to ``diff``,
``git``, etc. ``diff-hilite`` is based on the excellent difflib module
from Python standard library. The original version of the utility was
put together by Takeshi Komiya. Last-mile patching to make it a
drop-in replacement for ``diff`` is by Paul Sokolovsky.

Features
========

* Adds intra-line highlighting of differences to unified diff output.
* Serves as a (pipe) filter for output of ``diff -u`` and other tools
  producing diff output in "unified" format.

Install
=======

Use easy_install or pip::

   $ sudo easy_install diff-hilite

   Or

   $ sudo pip install diff-hilite

Applying to git
---------------

Add pager settings to your ``$HOME/.gitconfig`` to enable intra-line
highlighting::

   [pager]
       log = diff-hilite | less
       show = diff-hilite | less
       diff = diff-hilite | less


Applying to mercurial
---------------------

Add ``color`` and ``diff_highlight`` extensions to your ``$HOME/.hgrc`` to
enable intra-line highlighting::

   [extensions]
   color =
   diff_highlight =


Requirements
============

* Python 2.6 or 2.7, or Python 3.2, 3.3, 3.4 or higher
  (mercurial extension works on python 2.x only).


License
=======

Apache License 2.0 (``highlights/pprint.py`` is under PSFL).


History
=======

2.0
---
* Forked as ``diff-hilite``.
* Don't swallow arbitrary IOError's, swallow only EPIPE which happens
  often when using with interactive pagers like ``less``.
* Exit with the same result codes as ``diff`` (``diff | diff-hilite`` can
  be used as a drop-in replacement for just ``diff`` in scripts).

1.2.0 (2016-02-07)
-------------------
* Grouping indented hunks
* Fix #1: highlight if large text appended
* Fix mercurial extension has been broken since mercurial-3.7.0

1.1.0 (2015-07-12)
-------------------
* Drop py24 and py25 support
* Support git styled diff

1.0.3 (2015-03-30)
-------------------
* Ignore IOError on showing result

1.0.2 (2014-06-08)
-------------------
* Fix result of diff-highlight commannd is broken when diff-text includes new file
  (thanks @troter)

1.0.1 (2013-12-22)
-------------------
* Fix diff-highlight command failed with python 2.4

1.0.0 (2013-12-22)
-------------------
* Add diff-highlight command
* Support python 2.4, 2.5, 3.2 and 3.3

0.1.0 (2013-12-20)
-------------------
* first release
